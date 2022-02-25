#TG:ChauhanMahesh/DroneBots
#Github.com/vasusen-code

import asyncio
import time
import subprocess
import re
import os
import ffmpeg
from datetime import datetime as dt
from .. import Drone, BOT_UN
from telethon import events
from ethon.telefunc import fast_download, fast_upload
from ethon.pyfunc import video_metadata
from LOCAL.localisation import SUPPORT_LINK, JPG, JPG2, JPG3
from LOCAL.utils import ffmpeg_progress
from telethon.errors.rpcerrorlist import MessageNotModifiedError
from telethon.tl.types import DocumentAttributeVideo

async def encode(event, msg, scale=0):
    Drone = event.client
    edit = await Drone.send_message(event.chat_id, "Trying to process.", reply_to=msg.id)
    new_name = "out_" + dt.now().isoformat("_", "seconds")
    if hasattr(msg.media, "document"):
        file = msg.media.document
    else:
        file = msg.media
    mime = msg.file.mime_type
    if 'mp4' in mime:
        n = "media_" + dt.now().isoformat("_", "seconds") + ".mp4"
        out = new_name + ".mp4"
    elif msg.video:
        n = "media_" + dt.now().isoformat("_", "seconds") + ".mp4"
        out = new_name + ".mp4"
    elif 'x-matroska' in mime:
        n = "media_" + dt.now().isoformat("_", "seconds") + ".mkv" 
        out = new_name + ".mp4"            
    elif 'webm' in mime:
        n = "media_" + dt.now().isoformat("_", "seconds") + ".webm" 
        out = new_name + ".mp4"
    else:
        n = msg.file.name
        ext = (n.split("."))[1]
        out = new_name + ext
    DT = time.time()
    try:
        await fast_download(n, file, Drone, edit, DT, "**DOWNLOADING:**")
    except Exception as e:
        os.rmdir("encodemedia")
        print(e)
        return await edit.edit(f"An error occured while downloading.\n\nContact [SUPPORT]({SUPPORT_LINK})", link_preview=False) 
    name =  '__' + dt.now().isoformat("_", "seconds") + ".mp4"
    os.rename(n, name)
    await edit.edit("Extracting metadata...")
    vid = ffmpeg.probe(name)
    hgt = int(vid['streams'][0]['height'])
    wdt = int(vid['streams'][0]['width'])
    if scale == hgt:
        os.rmdir("encodemedia")
        return await edit.edit(f"The video is already in {scale}p resolution.")
    if scale == 240:
        if 426 == wdt:
            os.rmdir("encodemedia")
            return await edit.edit(f"The video is already in {scale}p resolution.")
    if scale == 360:
        if 640 == wdt:
            os.rmdir("encodemedia")
            return await edit.edit(f"The video is already in {scale}p resolution.")
    if scale == 480:
        if 854 == wdt:
            os.rmdir("encodemedia")
            return await edit.edit(f"The video is already in {scale}p resolution.")
    if scale == 720:
        if 1280 == wdt:
            os.rmdir("encodemedia")
            return await edit.edit(f"The video is already in {scale}p resolution.")
    FT = time.time()
    progress = f"progress-{FT}.txt"
    # -1:{scale} not working idk why
    nwdt = f"{int(wdt*hgt/scale)}"
    crf = {"240":"18", "360":"20", "480":"23", "720":"27"}
    cmd = f'ffmpeg -hide_banner -loglevel quiet -progress {progress} -i """{name}""" -c:v libx264 -pix_fmt yuv420p -preset ultrafast -s {str(nwdt)}x{str(scale)} -crf {str(crf[str(scale)])} -c:a libopus -ac 2 -ab 128k -c:s copy """{out}""" -y'
    try:
        await ffmpeg_progress(cmd, name, progress, FT, edit, '**ENCODING:**')
    except Exception as e:
        os.rmdir("encodemedia")
        print(e)
        return await edit.edit(f"An error occured while FFMPEG progress.\n\nContact [SUPPORT]({SUPPORT_LINK})", link_preview=False)   
    out2 = dt.now().isoformat("_", "seconds") + ".mp4" 
    if msg.file.name:
        out2 = msg.file.name
    else:
        out2 = dt.now().isoformat("_", "seconds") + ".mp4" 
    os.rename(out, out2)
    i_size = os.path.getsize(name)
    f_size = os.path.getsize(out2)
    text = f'**ENCODED by** : @{BOT_UN}\n\nbefore encoding : `{i_size}`\nafter ecoding : `{f_size}`'
    UT = time.time()
    if 'webm' in mime:
        try:
            uploader = await fast_upload(f'{out2}', f'{out2}', UT, Drone, edit, '**UPLOADING:**')
            await Drone.send_file(event.chat_id, uploader, caption=text, thumb=JPG, force_document=True)
        except Exception as e:
            os.rmdir("encodemedia")
            print(e)
            return await edit.edit(f"An error occured while uploading.\n\nContact [SUPPORT]({SUPPORT_LINK})", link_preview=False)
    elif 'x-matroska' in mime:
        try:
            uploader = await fast_upload(f'{out2}', f'{out2}', UT, Drone, edit, '**UPLOADING:**')
            await Drone.send_file(event.chat_id, uploader, caption=text, thumb=JPG, force_document=True)
        except Exception as e:
            os.rmdir("encodemedia")
            print(e)
            return await edit.edit(f"An error occured while uploading.\n\nContact [SUPPORT]({SUPPORT_LINK})", link_preview=False)
    else:
        metadata = video_metadata(out2)
        width = metadata["width"]
        height = metadata["height"]
        duration = metadata["duration"]
        attributes = [DocumentAttributeVideo(duration=duration, w=width, h=height, supports_streaming=True)]
        try:
            uploader = await fast_upload(f'{out2}', f'{out2}', UT, Drone, edit, '**UPLOADING:**')
            await Drone.send_file(event.chat_id, uploader, caption=text, thumb=JPG3, attributes=attributes, force_document=False)
        except Exception:
            try:
                uploader = await fast_upload(f'{out2}', f'{out2}', UT, Drone, edit, '**UPLOADING:**')
                await Drone.send_file(event.chat_id, uploader, caption=text, thumb=JPG, force_document=True)
            except Exception as e:
                os.rmdir("encodemedia")
                print(e)
                return await edit.edit(f"An error occured while uploading.\n\nContact [SUPPORT]({SUPPORT_LINK})", link_preview=False)
    await edit.delete()
    os.remove(name)
    os.remove(out2)
    
