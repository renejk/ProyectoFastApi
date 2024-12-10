import os
from dotenv import load_dotenv

load_dotenv()

class Config:
    DB_USER = os.getenv("DB_USER")
    DB_PASS = os.getenv("DB_PASS")
    DB_HOST = os.getenv("DB_HOST")
    DB_PORT = os.getenv("DB_PORT")
    DB_ENGINE = os.getenv("DB_ENGINE")
    DB_NAME = os.getenv("DB_NAME")

    DB_URL = f"{DB_ENGINE}://{DB_USER}:{DB_PASS}@{DB_HOST}:" \
                        f"{DB_PORT}/{DB_NAME}"



config = Config()