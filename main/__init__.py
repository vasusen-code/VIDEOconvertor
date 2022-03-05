#ChauhanMahesh/DroneBots/COL

from telethon import TelegramClient
from decouple import config
import logging
import time

logging.basicConfig(format='[%(levelname) 5s/%(asctime)s] %(name)s: %(message)s',
                    level=logging.WARNING)

# variables
API_ID = config("API_ID", default=None, cast=int)
API_HASH = config("API_HASH", default=None)
BOT_TOKEN = config("BOT_TOKEN", default=None)
BOT_UN = config("BOT_UN", default=None)
LIBRARY = config("LIBRARY", default="PYROGRAM")

from ethon.pyfunc import bash
if LIBRARY != "TELETHON":
    bash("pip install tgcrypto")
else:
    bash("pip install cryptg")
    
Drone = TelegramClient('bot', API_ID, API_HASH).start(bot_token=BOT_TOKEN) 

from pyrogram import Client

PyroBot = Client(
    "PyroClient",
    bot_token=BOT_TOKEN,
    api_id=int(API_ID),
    api_hash=API_HASH
)    

try:
    PyroBot.start()
except Exception as e:
    print(e)
    sys.exit(1)
