import os
from dotenv import load_dotenv

load_dotenv()


class Settings:
    TOKEN: str = os.getenv('TOKEN')
    PREFIX: str = os.getenv('PREFIX')


settings = Settings()
