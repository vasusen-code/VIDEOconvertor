#TG:ChauhanMahesh/DroneBots
#Github.com/Vasusen-code

import subprocess
import time
from telethon import events
from LOCLAL.localisation import SUPPORT_LINK, JPG
from ethon.telefunc import fast_download, fast_upload
from ethon.pyfunc import bash

async def mp3(event, msg):
    Drone = event.client
    edit = await Drone.send_message(even.chat_id, "Trying to process!", reply_to=msg.id)
    if hasattr(msg.media, "document"):
        file = msg.media.document
    else:
        file = msg.media
    mime = msg.file.mime_type
    if 'mp4' in mime:
        name = "media_" + dt.now().isoformat("_", "seconds") + ".mp4"
    elif msg.video:
        name = "media_" + dt.now().isoformat("_", "seconds") + ".mp4"
    elif 'x-matroska' in mime:
        name = "media_" + dt.now().isoformat("_", "seconds") + ".mkv" 
    elif 'webm' in mime:
        name = "media_" + dt.now().isoformat("_", "seconds") + ".webm"      
    else:
        name = msg.file.name
    try:
        await fast_download()
    except Exception as e:
        print(e)
        return await edit.edit(f"An error occured while downloading!\n\nContact [SUPPORT]({SUPPORT_LINK})')
    try:
        bash(f"ffmpeg -i {name} -codec:a libmp3lame -q:a 0 {out}.mp3')
    except Exception as e:
        print(e)
        return await edit.edit(f"An error occured while converting!\n\nContact [SUPPORT]({SUPPORT_LINK})')
    await fast_upload()
    await Drone.send_file()
                               
             
