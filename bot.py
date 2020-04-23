import discord
from discord.ext import commands
bot = commands.Bot(command_prefix='-')

counter = 1
@bot.command()
async def inc(ctx,):
	global counter
	counter = counter+1
@bot.command()
async def dec(ctx,):
	global counter
	counter = counter-1
@bot.command()
async def show(ctx,):
	global counter
	await ctx.send(counter)
bot.run('xxxxxxxxxxxx')