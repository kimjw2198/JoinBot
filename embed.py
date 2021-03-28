import discord
import datetime
import time
import asyncio
import os
import youtube_dl

from discord.ext import commands

client = discord.Client()

@client.event
async def on_message(message):
    if message.content.startswith(":입장"):
        await message.author.voice.channel.connent()
        await message.channel.send("보이스채널 입장")
        
access_token = os.environ['BOT_TOKEN']
client.run(access_token)
