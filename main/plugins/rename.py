#TG:ChauhanMahesh/DroneBots
#Github.com/Vasusen-code

import time
from datetime import datetime as dt
from .. import Drone, BOT_UN
from telethon import events
from ethon.telefunc import fast_download, fast_upload
from ethon.pyutils import rename
from ethon.pyfunc import video_metadata
from LOCAL.localisation import SUPPORT_LINK, JPG
from telethon.tl.types import DocumentAttributeVideo

async def media_rename(event, msg, new_name):
    edit = await event.client.send_message(event.chat_id, 'Trying to process.', reply_to=msg.id)
    Drone = event.client
    DT = time.time()
    mime = msg.document.mime_type
    if 'mp4' in mime:
        name = "media_" + dt.now().isoformat("_", "seconds") + ".mp4"
        out = new_name + dt.now().isoformat("_", "seconds") + ".mp4"
    elif 'x-matroska' in mime:
        name = "media_" + dt.now().isoformat("_", "seconds") + ".mkv" 
        out = new_name + dt.now().isoformat("_", "seconds") + ".mkv"            
    elif 'webm' in mime:
        name = "media_" + dt.now().isoformat("_", "seconds") + ".webm" 
        out = new_name + dt.now().isoformat("_", "seconds") + ".webm"
    elif 'zip' in mime:
        name = "media_" + dt.now().isoformat("_", "seconds") + ".zip" 
        out = new_name + dt.now().isoformat("_", "seconds") + ".zip"            
    elif 'jpg' in mime:
        name = "media_" + dt.now().isoformat("_", "seconds") + ".jpg" 
        out = new_name + dt.now().isoformat("_", "seconds") + ".jpg"
    elif 'png' in mime:
        name = "media_" + dt.now().isoformat("_", "seconds") + ".png"
        out = new_name + dt.now().isoformat("_", "seconds") + ".png"
    elif 'pdf' in mime:
        name = "media_" + dt.now().isoformat("_", "seconds") + ".pdf" 
        out = new_name + dt.now().isoformat("_", "seconds") + ".pdf"
    elif 'rar' in mime:
        name = "media_" + dt.now().isoformat("_", "seconds") + ".rar"
        out = new_name + dt.now().isoformat("_", "seconds") + ".rar"
    elif 'mp3' in mime:
        name = "media_" + dt.now().isoformat("_", "seconds") + ".mp3" 
        out = new_name + dt.now().isoformat("_", "seconds") + ".mp3"
    elif 'ogg' in mime:
        name = "media_" + dt.now().isoformat("_", "seconds") + ".ogg" 
        out = new_name + dt.now().isoformat("_", "seconds") + ".ogg"          
    elif 'flac' in mime:
        name = "media_" + dt.now().isoformat("_", "seconds") + ".flac"  
        out = new_name + dt.now().isoformat("_", "seconds") + ".flac"
    elif 'wav' in mime:
        name = "media_" + dt.now().isoformat("_", "seconds") + ".wav" 
        out = new_name + dt.now().isoformat("_", "seconds") + ".wav"
    elif 'webp' in mime:
        name = "media_" + dt.now().isoformat("_", "seconds") + ".webp" 
        out = new_name + dt.now().isoformat("_", "seconds") + ".webp"
    else:
        default_name = msg.file.name
        if not default_name:
            await edit.edit("Failed fetching extension of your file.")
        else:
            try:
                name = msg.file.name
                ext = (name.split("."))[1]
                out = new_name + "." + ext
                await fast_download(name, msg.media, Drone, edit, DT, "**DOWNLOADING:**")
                rename(name, out)
                UT = time.time()
                uploader = await fast_upload(out, msg.media, UT, Drone, edit, '**UPLOADING:**')
                net_time = round(DT - UT)
                await Drone.send_file(event.chat_id, uploader, caption=f"**Renamed by** : @{BOT_UN}\n\nTotal time:{net_time} seconds.", thumb=JPG, force_document=True)
            except Exception as e:
                await edit.edit(f"An error occured.\n\nContact [SUPPORT]({SUPPORT_LINK})", link_preview=False)
                print(e)
                return
    try:  
        await fast_download(name, msg.media, Drone, edit, DT, "**DOWNLOADING:**")
    except Exception as e:
        await edit.edit(f"An error occured while downloading.\n\nContact [SUPPORT]({SUPPORT_LINK})", link_preview=False)
        print(e)
        return
    await event.edit("Renaming.")
    try:
        rename(name, out)
    except Exception as e:
        await edit.edit(f"An error occured while renaming.\n\nContact [SUPPORT]({SUPPORT_LINK})", link_preview=False)
        print(e)
        return
    try:
        if not 'video' in mime:
            UT = time.time()
            uploader = await fast_upload(out, msg.media, UT, Drone, edit, '**UPLOADING:**')
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
                uploader = await fast_upload(out, msg.media, UT, Drone, edit, '**UPLOADING:**')
                net_time = round(DT - UT)
                await Drone.send_file(event.chat_id, uploader, caption=f"**Renamed by** : @{BOT_UN}\n\nTotal time:{net_time} seconds.", thumb=JPG, attributes=attr, force_document=False)
            else:
                UT = time.time()
                uploader = await fast_upload(out, msg.media, UT, Drone, edit, '**UPLOADING:**')
                net_time = round(DT - UT)
                await Drone.send_file(event.chat_id, uploader, caption=f"**Renamed by** : @{BOT_UN}\n\nTotal time:{net_time} seconds.", thumb=JPG, force_document=True)
    except Exception as e:
        await edit.edit(f"An error occured while uploading.\n\nContact [SUPPORT]({SUPPORT_LINK})", link_preview=False)
        print(e)
        return

    
