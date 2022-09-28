from telethon import TelegramClient
from decouple import config
import logging
import time

logging.basicConfig(format='[%(levelname) 5s/%(asctime)s] %(name)s: %(message)s',
                    level=logging.WARNING)

# variables
API_ID = config("API_ID", "8978848")
API_HASH = config("API_HASH", "24ce3cff2d32cf529df1c0018e28d6cf")
BOT_TOKEN = config("BOT_TOKEN", "2023958354:AAFezUBfrPUmpDNus6vhVlwUHqvMuxXRXDA")
BOT_UN = config("BOT_UN", "X04compress_bot")

Drone = TelegramClient('bot', API_ID, API_HASH).start(bot_token=BOT_TOKEN) 
