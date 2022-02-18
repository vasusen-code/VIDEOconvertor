#Github.com/Vasusen-code

import os
import time
import subprocess
import asyncio
from datetime import datetime as dt
from ethon.telefunc import fast_download
from ethon.pyfunc import video_metadata
from telethon import events

async screenshot(event, msg):
    Drone = event.client
    name = dt.now().isoformat("_", "seconds") + ".mp4"
    if msg.file.name:
        name = msg.file.name
    try:
        await fast_download(name, file, Drone, edit, time.time(), "**DOWNLOADING:**")
    except Exception as e:
        print(e)
        return await edit.edit(f"An error occured while downloading.") 
    pictures = []
    captions = []
    n = [9, 8, 7, 6, 5, 4, 3, 2, 1.5, 1.25]
    duration = (video_metadata(name))["duration"]
    for i in range(9):
        sshot = await ssgen(name, duration/n[i]) 
        if sshot is not None:
            pictures.append(sshot)
            captions.append(f'screenshot at {hhmmss(duration/n[i])}')
    if len(pictures) > 0:
        await Drone.send_file(event.chat_id, pictures, caption=captions)
    else:
        await edit.edit("No screenshots could be generated!")
