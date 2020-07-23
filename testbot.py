
import discord
import os

from discord.ext import commands

#holds the instance of our bot
client = commands.Bot(command_prefix = ".")

#event - code that exacutes when the bot detects something in perticular

#on_Ready function executes code when your bot is ready to use
@client.event
async def on_ready():
    print("I'm ready!")

@client.event
async def on_member_join(member):
    print(f'{member} has joined the server!')

@client.event
async def on_member_remove(member):
    print(f'{member} has left the server!')

#Token/API Key - a code that connects are code to our bot
client.run(os.environ.get('Bot token for Steve'))