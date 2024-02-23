import discord
import os
from dotenv import load_dotenv

# Define a dictionary mapping keywords to emoji names
emoji_mapping = {
    'ion': {'name': 'ion', 'animated': True},
    'amogus': {'name': 'amogus', 'animated': True},
    'brody': {'name': 'brody', 'animated': False}
}

class Bot(discord.Client):
    def __init__(self):
        super().__init__()
        self.synced = False

    async def on_ready(self):
        print(f'Logged in as {self.user.name}')

    async def on_message(self, message):
        alshor_user_id = int(os.getenv("ALSHOR"))
        if message.author.id == alshor_user_id:
            if '<@1130190164682080369>' in message.content.lower():
                for keyword, emoji_info in emoji_mapping.items():0
                    if emoji_info['name'] in message.content.lower() and emoji_info['animated']:
                        await self.add_emoji_reaction(message, emoji_info['name'])
        elif "<@1164059112737353798>" in message.content:
            await message.channel.send("nice words.")
        else:
            for keyword, emoji_info in emoji_mapping.items():
                if keyword in message.content.lower():
                    await self.add_emoji_reaction(message, emoji_info['name'], emoji_info['animated'])

    async def add_emoji_reaction(self, message, emoji_name, animated=False):
        emojis = [emoji for emoji in message.guild.emojis if emoji_name in emoji.name and (emoji.animated if animated else not emoji.animated)]
        for emoji in emojis:
            await message.add_reaction(emoji)

load_dotenv()
bot = Bot()
bot.run(os.getenv("DISCORD_TOKEN"))
