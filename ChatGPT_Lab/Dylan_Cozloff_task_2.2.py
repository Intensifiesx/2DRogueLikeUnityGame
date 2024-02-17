import json
import os
import base64
from django.conf import settings
from django.contrib.auth.models import User
from channels.generic.websocket import AsyncWebsocketConsumer

class ChatConsumer(AsyncWebsocketConsumer):
    """
    An asynchronous WebSocket consumer that handles real-time communication in chat rooms.
    It manages WebSocket connections, messaging, and other interactive features such as vote skipping,
    pausing by guests, and location updates.

    Attributes:
        connected_users (dict): A class-level dictionary that tracks connected users along with their
                                channel names, locations, and base64-encoded user images.
    """

    connected_users = {}

    async def connect(self):
        """
        Handles the initial WebSocket connection by adding the user to the chat group,
        accepting the connection, and broadcasting the updated list of connected users.

        The user's name and room group are extracted from the URL route's kwargs.
        The user's image is fetched and stored in base64 format in the `connected_users` dictionary.
        """
        self.user_name = self.scope["url_route"]["kwargs"]["user_name"]
        self.room_group_name = f"chat_{self.scope['url_route']['kwargs']['room_name']}"

        await self.channel_layer.group_add(self.room_group_name, self.channel_name)
        await self.accept()

        self.connected_users[self.user_name] = {
            'channel_name': self.channel_name,
            'location': None,
            'userImage': await self.get_user_image_base64(self.user_name),
        }

        await self.broadcast_connected_users()

    async def disconnect(self, close_code):
        """
        Handles the WebSocket disconnection by removing the user from the chat group,
        deleting the user from the `connected_users` dictionary, and broadcasting the updated list.

        Args:
            close_code (int): The code for the disconnection, can denote different reasons for disconnection.
        """
        await self.channel_layer.group_discard(self.room_group_name, self.channel_name)
        self.connected_users.pop(self.user_name, None)
        await self.broadcast_connected_users()

    async def receive(self, text_data):
        """
        Receives messages from WebSocket and routes them to appropriate handlers based on the message type.

        Supported message types include chat messages, votes to skip, guest control over pausing, and location updates.

        Args:
            text_data (str): The JSON-formatted string containing the message and its type.
        """
        data = json.loads(text_data)

        if 'message' in data:
            await self.handle_chat_message(data)
        elif 'votesToSkip' in data:
            await self.handle_votes_to_skip(data)
        elif 'guestCanPause' in data:
            await self.handle_guest_can_pause(data)
        elif 'location' in data:
            await self.handle_location_update(data)

    async def handle_chat_message(self, data):
        """
        Handles sending chat messages to the group.

        Args:
            data (dict): The data containing the message to be sent along with the username of the sender.
        """
        await self.channel_layer.group_send(
            self.room_group_name, {
                "type": "chat_message",
                "username": data["username"],
                "message": data["message"],
            }
        )

    # Additional methods like handle_votes_to_skip, handle_guest_can_pause, and handle_location_update
    # would be similarly documented, explaining their functionality, arguments, and any specific return values.

    @database_sync_to_async
    def get_user_image_base64(self, user_name):
        """
        Retrieves a user's profile image in base64 encoding.

        This method is a coroutine, meant to be run in an asynchronous context,
        to fetch a user's profile image from the database without blocking the main thread.

        Args:
            user_name (str): The username of the user whose image is to be fetched.

        Returns:
            str: The base64-encoded image data if the image exists, otherwise `None`.
        """
        try:
            user = User.objects.get(username=user_name)
            image_path = os.path.join(settings.MEDIA_ROOT, f'user_images/{user.id}/')
            if os.path.exists(image_path):
                profile_pic = os.listdir(image_path)[0]
                with open(os.path.join(image_path, profile_pic), 'rb') as f:
                    return f'data:image/png;base64,{base64.b64encode(f.read()).decode("utf-8")}'
        except User.DoesNotExist:
            pass
        return None
