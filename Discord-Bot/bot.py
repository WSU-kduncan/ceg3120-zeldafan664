# Based on example https://discordpy.readthedocs.io/en/stable/quickstart.html
import os

import discord
import random
from dotenv import load_dotenv

intents = discord.Intents.default()
intents.message_content = True

load_dotenv()
TOKEN = os.getenv('DISCORD_TOKEN')
GUILD = os.getenv('DISCORD_GUILD')

client = discord.Client(intents=intents)

@client.event
async def on_ready():
    print(f'{client.user} has connected to Discord!')

    for guild in client.guilds:
        if guild.name == GUILD:
            break

    print(
        f'{client.user} is connected to the following guild:\n'
        f'{guild.name}(id: {guild.id})'
    )

@client.event
async def on_message(message):
    if message.author == client.user:
        return

    flowey_Quotes = [ " Howdy! I'm FLOWEY. FLOWEY the FLOWER! Your new best friend!",
            " Wow, you're utterly repulsive.",
            " You spared her life...", 
            " Then you decided that just wasn't interesting enough for you." ]
    if message.content == 'howdy!':
    #if message.content.startswith('$howdy'):
        response = random.choice(flowey_Quotes)
        await message.channel.send(response)

client.run(TOKEN)
