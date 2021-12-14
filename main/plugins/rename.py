#TG:ChauhanMahesh/DroneBots
#Github.com/Vasusen-code

import time
from datetime import datetime as dt
from .. import Drone, BOT_UN
from telethon import events
from ethon.telefunc import fast_download, fast_upload
from ethon.pyutils import rename
from ethon.pyfunc import video_metadata
from LOCAL.localisation import SUPPORT_LINK, JPG, 
from telethon.tl.types import DocumentAttributeVideo

async def media_rename(event, msg, new_name):
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
        default_name = msg.file.name
        if not default_name:
            await event.edit("Failed fetching extension of your file.")
        else:
            try:
                name = msg.file.name
                ext = (name.split("."))[1]
                out = new_name + "." + ext
                await Drone.fast_download(name, msg.media, Drone, event, DT, "**DOWNLOADING:**")
                rename(name, out)
                UT = time.time()
                uploader = await fast_upload(name, msg.media, UT, Drone, event, '**UPLOADING:**')
                net_time = round(DT - UT)
                await Drone.send_file(event.chat_id, uploader, caption=f"**Renamed by** : @{BOT_UN}\n\nTotal time:{net_time} seconds.", thumb=JPG, force_document=True)
            except Exception as e:
                await event.edit(f"An error occured.\n\nContact [SUPPORT]({SUPPORT_LINK})")
                print(e)
                return
    try:  
        await Drone.fast_download(name, msg.media, Drone, event, DT, "**DOWNLOADING:**")
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
            uploader = await fast_upload(name, msg.media, UT, Drone, event, '**UPLOADING:**')
            net_time = round(DT - UT)
            await Drone.send_file(event.chat_id, uploader, caption=f"**Renamed by** : @{BOT_UN}\n\nTotal time:{net_time} seconds.", thumb=JPG, force_document=True)
        else:
            if 'mp4' in mime:
                metadata = video_metadata(msg.media)
                width = metadata["width"]
                height = metadata["height"]
                duration = metadata["duration"]
                attr = [DocumentAttributeVideo(duration=int(duration), w=width, h=height, supports_streaming=True)]
                UT = time.time()
                uploader = await fast_upload(name, msg.media, UT, Drone, event, '**UPLOADING:**')
                net_time = round(DT - UT)
                await Drone.send_file(event.chat_id, uploader, caption=f"**Renamed by** : @{BOT_UN}\n\nTotal time:{net_time} seconds.", thumb=JPG, attributes=attr, force_document=False)
            else:
                UT = time.time()
                uploader = await fast_upload(name, msg.media, UT, Drone, event, '**UPLOADING:**')
                net_time = round(DT - UT)
                await Drone.send_file(event.chat_id, uploader, caption=f"**Renamed by** : @{BOT_UN}\n\nTotal time:{net_time} seconds.", thumb=JPG, force_document=True)
    except Exception as e:
        await event.edit(f"An error occured while uploading.\n\nContact [SUPPORT]({SUPPORT_LINK})")
        print(e)
        return

    
