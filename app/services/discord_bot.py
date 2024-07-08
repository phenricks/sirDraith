import os
import threading
import asyncio
import discord

from discord.ext import commands
from app.core.config import settings

intents = discord.Intents.default()
bot = commands.Bot(command_prefix=os.getenv('PREFIX'), intents=intents)


@bot.event
async def on_ready():
    print(f'Logged in as {bot.user}')


@bot.command(name='teste')
async def perry(ctx):
    await ctx.send(
                "🌙✨ Saudações, viajante das sombras. Eu sou **SirDraith**, o **Tecelão das Noites**, guardião dos segredos da escuridão. Em meu domínio, a noite é tanto uma proteção quanto uma arma. 🌌🔮\n\n"
                "Aqui, encontrarás sabedoria antiga e poder além da imaginação. 🧙‍♂️📜 As estrelas cintilam com segredos antigos, e os ventos sussurram histórias de magia esquecida. ✨🌟\n\n"
                "Caminhe com respeito e coração puro, e as trevas te acolherão como um aliado. 🌑💫 Sinta-se em casa no nosso reino encantado, onde a lua guia nossos passos e a magia flui como um rio de luz negra.\n\n"
                "🌠 Seja bem-vindo ao nosso reino, onde a aventura te aguarda a cada esquina. 🏰⚔️"
            )


@bot.command(name='ping')
async def ping(ctx):
    await ctx.send('Pong!')


def run_bot():
    loop = asyncio.new_event_loop()
    asyncio.set_event_loop(loop)
    try:
        loop.run_until_complete(bot.start(settings.DISCORD_TOKEN))
    except RuntimeError as e:
        print(f'Error running bot: {e}')
    finally:
        loop.run_until_complete(loop.shutdown_asyncgens())
        loop.close()


def start_bot_thread():
    bot_thread = threading.Thread(target=run_bot, name='BotThread')
    bot_thread.start()
    return bot_thread


def stop_bot():
    loop = asyncio.get_event_loop()
    asyncio.run_coroutine_threadsafe(bot.close(), bot.loop)
    bot.loop.call_soon_threadsafe(bot.loop.stop)
