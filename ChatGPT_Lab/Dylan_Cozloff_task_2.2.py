import json
import os
import base64
from django.conf import settings
from django.contrib.auth.models import User
from django.core import serializers
from asgiref.sync import async_to_sync, sync_to_async
from channels.db import database_sync_to_async
from channels.consumer import StopConsumer

from channels.generic.websocket import AsyncWebsocketConsumer


class ChatConsumer(AsyncWebsocketConsumer):

    connected_users = {}

    async def connect(self):
        self.room_name = self.scope["url_route"]["kwargs"]["room_name"]
        self.user_name = self.scope["url_route"]["kwargs"]["user_name"]
        self.room_group_name = "chat_%s" % self.room_name

        # Join room group
        await self.channel_layer.group_add(self.room_group_name, self.channel_name)
        await self.accept()

        user_image = await database_sync_to_async(self.get_user_image)(self.user_name)

        # Add user to the list of connected users
        self.connected_users[self.user_name] = {
            'channel_name': self.channel_name,
            'location': None,
            'userImage': 'data:image/png;base64,' + user_image,
        }

        # Send connected users to the client
        await self.send_connected_users()

    @staticmethod
    def get_user_image(user_name):
        try:
            user = User.objects.get(username=user_name)
            user_id = user.id
        except User.DoesNotExist:
            return None
    
        image_path = os.path.join(settings.MEDIA_ROOT, f'user_images/{user_id}/')
        if os.path.exists(image_path):
            profile_pic = os.listdir(image_path)[0]
            file_path = os.path.join(image_path, profile_pic)
            with open(file_path, 'rb') as f:
                encoded_image = base64.b64encode(f.read()).decode('utf-8')
                return encoded_image
        else:
            return None

        
    # Leave room group
    async def disconnect(self, close_code):
        await self.channel_layer.group_discard(self.room_group_name, self.channel_name)

        # Remove user from the list of connected users
        if self.user_name in self.connected_users:
            del self.connected_users[self.user_name]

        # Send connected users to the client
        await self.send_connected_users()

        raise StopConsumer()


    # Receive message from WebSocket
    async def receive(self, text_data):
        text_data_json = json.loads(text_data)
        username = ""
        message = ""
        votesToSkip = ""
        guestCanPause = ""

        if 'message' in text_data_json:
            message = text_data_json["message"]
            username = text_data_json["username"]
        if 'votesToSkip' in text_data_json:
            votesToSkip = text_data_json["votesToSkip"]

            # Update votesToSkip for the group
            await self.channel_layer.group_send(
                self.room_group_name,
                {
                    'type': 'update_votes_to_skip',
                    'votesToSkip': votesToSkip
                }
            )
        if 'guestCanPause' in text_data_json:
            guestCanPause = text_data_json["guestCanPause"]
            # Update guestCanPause for the group
            await self.channel_layer.group_send(
                self.room_group_name,
                {
                    'type': 'update_guestCanPause',
                    'guestCanPause': guestCanPause
                }
            )

        if 'votesToSkip' not in text_data_json and 'guestCanPause' not in text_data_json:
            await self.channel_layer.group_send(
                self.room_group_name, {
                    "type": "chat_message", 
                    "username": username, 
                    "message": message,
                }
        )
        
        if 'location' in text_data_json:
            location = text_data_json["location"]
            username = text_data_json["username"]
            if username in self.connected_users:
                self.connected_users[username]['location'] = location
                await self.send_connected_users()


    # Receive message from room group
    async def chat_message(self, event):
        message = event["message"]
        username = event["username"]
        messageColor = "#ffffff"

        user_image = self.connected_users.get(username, {}).get('userImage', '')

        if username:
            # Send message to WebSocket
            await self.send(text_data=json.dumps({
                "message": message,
                "username": username,
                "messageColor": messageColor,
                "userImage": user_image
                }))

    async def send_connected_users(self):
        # Send updated connected users list to all clients in the room group
        await self.channel_layer.group_send(
            self.room_group_name, {"type": "connected_send", "users": self.connected_users}
        )

    async def connected_send(self, event):
        # Send updated connected users list to all clients in the room group
        await self.send(text_data=json.dumps({
            'type': 'connected_users',
            'users': event["users"],
        }))

    async def update_votes_to_skip(self, event):
        votesToSkip = event['votesToSkip']

        # Send the updated votesToSkip value to all users in the group
        await self.send(text_data=json.dumps({
            'type': 'votesToSkip',
            'votesToSkip': votesToSkip
        }))

    async def update_guestCanPause(self, event):
        guestCanPause = event['guestCanPause']

        # Send the updated guestCanPause value to all users in the group
        await self.send(text_data=json.dumps({
            'type': 'guestCanPause',
            'guestCanPause': guestCanPause
        }))