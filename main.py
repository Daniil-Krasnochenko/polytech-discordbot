import json

import discord
from discord.ext import commands
intents = discord.Intents.all()
file = open('config.json', 'r')
config = json.load(file)
bot = commands.Bot(config['prefix'],intents=intents)
@bot.command(name = 'com1')
async def com1(ctx):
    await ctx.send(f'{ctx.author.mention}Hi!')
@bot.command(name = 'button')
async def button(ctx):
    button = discord.ui.Button(label='Authorization!', style=discord.ButtonStyle.green)
    view = discord.ui.View()
    view.add_item(button)
    await ctx.send('Here is a button:', view=view)
bot.run(config['token'])