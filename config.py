# - *- coding: utf- 8 - *-
import os
from dotenv import load_dotenv, find_dotenv


load_dotenv(find_dotenv())

BOT_TOKEN = os.getenv('BOT_TOKEN')
DB_NAME = os.getenv('DB_NAME')
USER = os.getenv('USER')
PASSWORD = os.getenv('PASSWORD')
HOST = os.getenv('HOST')
BOT_ADMIN = []
