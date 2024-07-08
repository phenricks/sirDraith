import threading
from typing import Optional

from fastapi import APIRouter

from app.model.response_api import ResponseApi
from app.services.discord_bot import start_bot_thread, stop_bot

router = APIRouter()

response = ResponseApi()

bot_thread = None


@router.get('/start-bot')
async def start_bot_endpoint():
    global bot_thread
    if bot_thread is None or not bot_thread.is_alive():
        bot_thread = start_bot_thread()
        return response.create_response('Bot started')
    else:
        return response.create_response('Bot is already running')


@router.get('/stop-bot')
async def stop_bot_endpoint():
    global bot_thread
    if bot_thread is not None and bot_thread.is_alive():
        stop_bot()
        bot_thread.join()
        bot_thread = None
        return response.create_response('Bot stopped')
    else:
        return response.create_response('Bot is not running')
