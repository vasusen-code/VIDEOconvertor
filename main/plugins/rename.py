#TG:ChauhanMahesh/DroneBots
#Github.com/Vasusen-code

import time
from datetime import datetime as dt
from .. import Drone
from telethon import events
from ethon.telefunc import fast_download, fast_upload
from ethon.pyutils import rename
from ethon.pyfunc import video_metadata
from LOCAL.localisations import SUPPORT_LINK

async def media_rename(event, msg, out):
    await event.edit('Trying to process
    Drone = event.client
    DT = time.time()
    mime = msg.document.mime_type
    if 'mp4' in mime:
        name =  "media_" + dt.now().isoformat("_", "seconds") + ".mp4"
    elif 'x-matroska' in mime:
        name = "media_" + dt.now().isoformat("_", "seconds") + ".mkv" 
    elif 'webm' in mime:
        name = "media_" + dt.now().isoformat("_", "seconds") + ".webm" 
    elif 'zip' in mime:
        name = "media_" + dt.now().isoformat("_", "seconds") + ".zip" 
    elif 'jpg' in mime:
        name = "media_" + dt.now().isoformat("_", "seconds") + ".jpg" 
    elif 'png' in mime:
        name = "media_" + dt.now().isoformat("_", "seconds") + ".png" 
    elif 'pdf' in mime:
        name = "media_" + dt.now().isoformat("_", "seconds") + ".pdf" 
    elif 'rar' in mime:
        name = "media_" + dt.now().isoformat("_", "seconds") + ".rar" 
    elif 'mp3' in mime:
        name = "media_" + dt.now().isoformat("_", "seconds") + ".mp3" 
    elif 'ogg' in mime:
        name = "media_" + dt.now().isoformat("_", "seconds") + ".ogg" 
    elif 'flac' in mime:
        name = "media_" + dt.now().isoformat("_", "seconds") + ".flac"   
    elif 'wav' in mime:
        name = "media_" + dt.now().isoformat("_", "seconds") + ".wav" 
    elif 'webp' in mime:
        name = "media_" + dt.now().isoformat("_", "seconds") + ".webp" 
    else:
    try:  
        await Drone.fast_download(name, media, Drone, event, DT, "**DOWNLOADING:**")
    except Exception as e:
        await event.edit(f"An error occured while downloading.\n\nContact [SUPPORT]({SUPPORT_LINK})")
        print(e)
        return
    await event.edit("Renaming.")
    try:
        rename(name, out)
    except Exception as e:
        await event.edit(f"An error occured while renaming.\n\nContact [SUPPORT]({SUPPORT_LINK})")
        print(e)
        return
    try:
        if not 'video' in mime:
            UT = time.time()
            uploader = await fast_upload()
            await Drone.send_file(event.chat_id, uploader, caption="**Renamed by** {BOT_UN}\n\nTotal time:{net_time}, thumb=JPG, force_document=True)
        else:
    except Exception as e:
        await event.edit(f"An error occured while uploading.\n\nContact [SUPPORT]({SUPPORT_LINK})")
        print(e)
        return

    
