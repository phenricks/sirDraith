from fastapi import FastAPI
from app.api.endpoints import bot_commands
from app.model.response_api import ResponseApi

app = FastAPI()

response = ResponseApi()

app.include_router(bot_commands.router, prefix='/bot', tags=['bot'])


@app.get("/")
async def read_root():
    return response.create_response('Welcome to the Discord Bot API')
