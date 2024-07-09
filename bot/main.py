from fastapi import FastAPI
from bot.commands import commands
from bot.response.response_api import ResponseApi

app = FastAPI()

response = ResponseApi()

app.include_router(commands.router, prefix='/bot', tags=['bot'])


@app.get("/")
def read_root():
    return response.create_response('RPG Bot is running!')
