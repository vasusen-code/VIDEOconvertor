#TG:ChauhanMahesh/DroneBots
#Github.com/Vasusen-code

import time
from .. import Drone
from telethon import events
from ethon.telefunc import fast_download, fast_upload
from ethon.pyfunc import video_metadata

async def media_rename(event, msg):
    Drone = event.client
    DT = time.time()
    mime = msg.document.mime_type
    if 'mp4' in mime:
    await Drone.fast_download(media, Drone, event, DT, "**DOWNLOADING:**")
       
    
