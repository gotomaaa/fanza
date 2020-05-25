import discord
import config
import fanza
from datetime import datetime
from discord.ext import commands


tk = config.TOKEN
bot = commands.Bot(command_prefix='!')

@bot.event
async def on_ready():
    # 起動したらターミナルにログイン通知が表示される
    print('お天気お姉さんログインしました。')

@bot.command()
async def nuki(ctx, arg):
    videos = fanza.getFanzaItem(arg)
    for i in range(3):
        message = "\nタイトル: " + videos['result']['items'][i]['title'] + "\nURL: " + videos['result']['items'][i]['affiliateURL']
        await ctx.send(message)

bot.run(tk)
