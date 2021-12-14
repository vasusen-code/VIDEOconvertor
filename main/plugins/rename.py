#TG:ChauhanMahesh/DroneBots
#Github.com/Vasusen-code

import time
from .. import Drone
from telethon import events
from ethon.telefunc import fast_download, fast_upload
from ethon.pyfunc import video_metadata

async def media_rename(event, media):
    Drone = event.client
    await Drone.fast_download(media, Drone, event, DT, "**DOWNLOADING:**")
    
