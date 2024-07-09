from fastapi import APIRouter

from bot.bot import run_bot, shutdown_bot
from bot.response.response_api import ResponseApi

import asyncio

router = APIRouter()

response = ResponseApi()

bot_task = None


@router.post('/start-bot/')
async def start_bot_endpoint():
    global bot_task
    if bot_task is None or bot_task.done():
        loop = asyncio.get_event_loop()
        bot_task = loop.create_task(run_bot())
        return response.create_response('Bot started')
    return response.create_response('Bot is already running')


@router.post('/stop-bot/')
async def stop_bot_endpoint():
    await shutdown_bot()
    return response.create_response('Bot stopped')
