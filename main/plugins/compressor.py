#TG:ChauhanMahesh/DroneBots
#Github.com/vasusen-code

import asyncio
import time
import subprocess
import re
from datetime import datetime as dt
from .. import Drone, BOT_UN
from telethon import events
from ethon.telefunc import fast_download, fast_upload
from LOCAL.localisation import SUPPORT_LINK
#from LOCAL.utils import ffmpeg_progress
from telethon.errors.rpcerrorlist import MessageNotModifiedError
from telethon.tl.types import DocumentAttributeVideo
