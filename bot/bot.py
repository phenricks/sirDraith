import discord
from discord.ext import commands
from bot.config import settings

intents = discord.Intents.default()
intents.members = True
intents.messages = True
intents.reactions = True

bot = commands.Bot(command_prefix=settings.PREFIX, intents=intents)


@bot.event
async def on_ready():
    print(f'Logged in as {bot.user}')


def setup_bot():
    pass


async def run_bot():
    setup_bot()
    await bot.start(settings.TOKEN)


async def shutdown_bot():
    await bot.close()
