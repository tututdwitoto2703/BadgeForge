#badge modules
from badge.badge_final import banner_1
# from io import BytesIO


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
        await msg.channel.send(msg.content)
    if "https://tenor.com/view" in msg.content.lower():
        await msg.channel.send(f"Message from {msg.author} has attachments.")
        await msg.channel.send(msg.content)
    # adding attachments directly in the code
    # if msg.attachments:
    #         await msg.channel.send(f"Message from {msg.author.mention} has attachments.")
    #         for attachment in msg.attachments:
    #             await msg.channel.send(f"Attachment name: {attachment.filename}")
    #             await msg.channel.send((f"Attachment URL: {attachment.url}"))
    await bot.process_commands(msg)

@bot.command()
async def ping(ctx):
    await ctx.send(f"🏓 pong {round(bot.latency * 1000)}ms")

@bot.command()
async def create(ctx, *, content=None):
    attachments = ctx.message.attachments
    if attachments:
        first_file = attachments[0]
        await ctx.send(f"Attachment Detected: {first_file.url}")
        file_bytes = await first_file.read()
        
    else:
        await ctx.send("No Attachment Detected!!!")
        return
    if content:
        content_item = [x.split('=')[-1].strip() for x in content.split("\n")]

        await ctx.send(f"{content_item}")
    else:
        await ctx.send("Please Send content in the specified format i.e. \n```\n$create\nname=Name_of_application\ndesc=Project_Description\nfooter=Footer_Part\n```\n")
    

    output_buffer = await banner_1(file_bytes, content_item[0], content_item[1], content_item[-1] )
    output_buffer.seek(0)
    discord_file = discord.File(fp=output_buffer, filename=f"Badge_{content_item[0]}.png")
    await ctx.send("Here is your edited image:", file=discord_file)

#todo - save the attachments temporarily and only save if less than 8mb 
# and delete after 3mins(or wtv depending on time) 
bot.run(token, log_handler=handler, log_level=logging.DEBUG)

