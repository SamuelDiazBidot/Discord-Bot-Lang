import discord
from discord.ext import commands
bot = commands.Bot(command_prefix='-')

counter = 1
@bot.command()
async def inc(ctx,):
	global counter
	counter = counter+1
@inc.error
async def inc_error(ctx,error):
	if isinstance(error, commands.BadArgument):
		await ctx.send('Invalid Arguments')
@bot.command()
async def dec(ctx,):
	global counter
	counter = counter-1
@dec.error
async def dec_error(ctx,error):
	if isinstance(error, commands.BadArgument):
		await ctx.send('Invalid Arguments')
@bot.command()
async def show(ctx,):
	global counter
	await ctx.send(counter)
@show.error
async def show_error(ctx,error):
	if isinstance(error, commands.BadArgument):
		await ctx.send('Invalid Arguments')
@bot.command()
async def sum(ctx,x,y):
	result = int(x)+int(y)
	await ctx.send(result)
@sum.error
async def sum_error(ctx,error):
	if isinstance(error, commands.BadArgument):
		await ctx.send('Invalid Arguments')
bot.run('NzAxODA3MzU4NjYxMDk5NTgy.XrMWEA.D10sg4j1LjIhLJycz_rzaZVqr-4')