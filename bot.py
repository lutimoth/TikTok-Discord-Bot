import os

import discord
from discord.ext import commands
from dotenv import load_dotenv

#from TikTokApi import TikTokApi

cookie = {
  "s_v_web_id": "verify_ktue8vie_2Rzveakn_YpDn_4bu3_8PCj_AwsWhPeFj73l",
  "tt_webid": "1%7CipXkLWzChYfRyMVw9HH2M1wpV3xsbysjMhft5Oa8iA4%7C1632266170%7C6e1a9ef8886a1d0823e95a9b49119220eb710b3eea005dc21d9176b5975b363d"
}

load_dotenv()
TOKEN = os.getenv('TOKEN')
intents = discord.Intents.default()

bot = commands.Bot(command_prefix='!')

#verifyFp = "verify_ktswr95c_mSSa5qC2_mvku_4S0x_9Hnn_oCUJAqVl9fvg"

#tiktok = TikTokApi.get_instance(custom_verifyFp=verifyFp, use_test_endpoints = True)
#user = "naturesbless"

@bot.event
async def on_ready():
    print(f'{bot.user.name} has connected to Discord!')

@bot.command(name='recent')
async def message(ctx):
    await ctx.send('this is working, sort of')

bot.run(TOKEN)
