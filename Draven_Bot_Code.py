import discord
from discord.ext import commands
import json

intents = discord.Intents.default()
intents.message_content = True

bot = commands.Bot(command_prefix='$', intents=intents)

@bot.command()
async def test(ctx, arg):
    await ctx.send(arg)

bot.run('MTA2MzY3MTY1NzU5Nzc3NTkzMg.GX_OoF.208yZBxQjALn8fvA8g365IKTfi6YnlrhYoyr9I')