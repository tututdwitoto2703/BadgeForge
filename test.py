import discord
from discord.ext import commands
import logging
import os
from dotenv import load_dotenv
import time
load_dotenv()
token = os.getenv("DISCORD_TOKEN")

filenamerfn = "logs_" + time.strftime(("%a_%d-%H:%M")) + ".log"
handler = logging.FileHandler(filename=f'./logs/{filenamerfn}', mode="w", encoding="utf-8")
intents = discord.Intents.default()
intents.message_content = True
intents.members = True

bot = commands.Bot(command_prefix="$", intents=intents)

@bot.event
async def on_ready():
    print(f"Bot is read! yaya {bot.user}")

@bot.event
async def on_message(msg):

    if msg.author == bot.user:
        return
    if "YOYOYO".lower() in msg.content.lower():
        await msg.channel.send(f"waddup {msg.author.mention} {msg}")
    if "https://cdn.discordapp.com/attachments" in msg.content.lower():
        await msg.channel.send(f"Message from {msg.author} has attachments.")
        await msg.channel.send(msg.content.lower())
    if "https://tenor.com/view" in msg.content.lower():
        await msg.channel.send(f"Message from {msg.author} has attachments.")
        await msg.channel.send(msg.content.lower())
    if msg.attachments:
            await msg.channel.send(f"Message from {msg.author.mention} has attachments.")
            for attachment in msg.attachments:
                await msg.channel.send(f"Attachment name: {attachment.filename}")
                await msg.channel.send((f"Attachment URL: {attachment.url}"))
    await bot.process_commands(msg)

@bot.command()
async def ping(ctx):
    await ctx.send(f"pong ")
    

bot.run(token, log_handler=handler, log_level=logging.DEBUG)

