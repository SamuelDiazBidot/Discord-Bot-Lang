import discord
from discord.ext import commands
client = discord.Client()
bot = commands.Bot(command_prefix='$')
@bot.command()
async def send(ctx,arg):
	send(arg)
bot.add_command(send)

client.run('your token here')