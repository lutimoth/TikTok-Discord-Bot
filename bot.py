import os

import discord
from discord.ext import commands
from dotenv import load_dotenv
from TikTokApi import TikTokApi

api = TikTokApi.get_instance()

load_dotenv()
TOKEN = os.getenv('TOKEN')
intents = discord.Intents.default()

bot = commands.Bot(command_prefix='!')


@bot.event
async def on_ready():
    print(f'{bot.user.name} has connected to Discord!')


@bot.command(name='recent')
async def _command(ctx):
    global times_used
    await ctx.send('Please input your TikTok Username')

    def check(msg):
        return msg.author == ctx.author and msg.channel == ctx.channel

    msg = await bot.wait_for('message', check=check)
    userinfo = api.by_username(input(msg), count=1)
    for tiktok in userinfo:
        url = ('https://www.tiktok.com/@'+msg+'/video/'+tiktok['id'])
    await ctx.send(url)

bot.run(TOKEN)
