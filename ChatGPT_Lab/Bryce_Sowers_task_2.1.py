import discord, os, os.path
from discord.ext import commands, tasks
from dotenv import load_dotenv

class Bot(commands.Bot):
    def __init__(self):
        intents = discord.Intents.all()
        super().__init__(command_prefix='!', intents=intents, help_command=None)
        self.synced = False
    
    async def syncing(self):
        if not self.synced:
            await self.tree.sync()
            self.synced = True
        print(f"Synced slash commands for {self.user}.")   
        
    async def on_command_error(self, ctx, error):
        await ctx.reply(error, ephemeral=True)

load_dotenv()
bot = Bot()
partial_name = 'ion'
amogus_name = 'amogus'
brody_name = 'brody'
emoji_id_dict = []

@bot.event
async def on_ready():
    print(f'Logged in as {bot.user.name}')

@bot.event
async def on_message(message):
    alshor_user_id = int(os.getenv("ALSHOR"))
    #Checks for Alshor as a user and then checks if he has mentioned "@Team Uhhhhhh" or has said the word Geige.
    if message.author.id == alshor_user_id:
        if '<@1130190164682080369>' in message.content.lower():
            animated_ion_emojis = [emoji for emoji in message.guild.emojis if partial_name in emoji.name and emoji.animated]
            for items in animated_ion_emojis:
                await message.add_reaction(items)
    #Checks if the bot has been mentioned
    elif "<@1164059112737353798>" in message.content:
        await message.channel.send("fuck you.")
    elif 'geige' in message.content.lower():
        animated_ion_emojis = [emoji for emoji in message.guild.emojis if partial_name in emoji.name and emoji.animated]
        for items in animated_ion_emojis:
            await message.add_reaction(items)
    elif 'amogus' in message.content.lower():
        animated_ion_emojis = [emoji for emoji in message.guild.emojis if amogus_name in emoji.name and emoji.animated]
        for items in animated_ion_emojis:
            await message.add_reaction(items)
    elif 'brody' in message.content.lower():
        animated_ion_emojis = [emoji for emoji in message.guild.emojis if brody_name in emoji.name]
        for items in animated_ion_emojis:
            await message.add_reaction(items)
    else:
        print("No correct input found")
                
bot.run(os.getenv("DISCORD_TOKEN"))