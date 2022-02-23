#TG:ChauhanMahesh/DroneBots
#Github.com/vasusen-code

import asyncio
import time
import subprocess
import re
import os
import ffmpeg
from datetime import datetime as dt
from .. import Drone, BOT_UN, LOG_CHANNEL
from telethon import events
from ethon.telefunc import fast_download, fast_upload
from ethon.pyfunc import video_metadata
from LOCAL.localisation import SUPPORT_LINK, JPG, JPG2, JPG3
from LOCAL.utils import ffmpeg_progress
from telethon.errors.rpcerrorlist import MessageNotModifiedError
from telethon.tl.types import DocumentAttributeVideo
from main.plugins.actions import LOG_START, LOG_END

async def encode(event, msg, scale=0):
    ps_name = str(f"**{scale}p ENCODING:**")
    _ps = str(f"{scale}p ENCODE")
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
    log = await LOG_START(event, f'**{_ps} PROCESS STARTED**\n\n[Bot is busy now]({SUPPORT_LINK})')
    log_end_text = f'**{_ps} PROCESS FINISHED**\n\n[Bot is free now]({SUPPORT_LINK})'
    try:
        await fast_download(n, file, Drone, edit, DT, "**DOWNLOADING:**")
    except Exception as e:
        os.rmdir("encodemedia")
        await log.delete()
        await LOG_END(event, log_end_text)
        print(e)
        return await edit.edit(f"An error occured while downloading.\n\nContact [SUPPORT]({SUPPORT_LINK})", link_preview=False) 
    name = '__' + dt.now().isoformat("_", "seconds") + ".mp4"
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
    cmd = ''
    # Bitrates choosed from recommended bitrates on google's official blog for youtube
    if scale == 240:
        cmd = f'ffmpeg -hide_banner -loglevel quiet -progress {progress} -i """{name}""" -filter:v scale="-2:240" -b:v 400k -c:a copy """{out}""" -y'
    elif scale == 360:
        cmd = f'ffmpeg -hide_banner -loglevel quiet -progress {progress} -i """{name}""" -filter:v scale="-2:360" -b:v 750k -c:a copy """{out}""" -y'
    elif scale == 480:
        cmd = f'ffmpeg -hide_banner -loglevel quiet -progress {progress} -i """{name}""" -filter:v scale="-2:480" -b:v 1000k -c:a copy """{out}""" -y'
    elif scale == 720:
        cmd = f'ffmpeg -hide_banner -loglevel quiet -progress {progress} -i """{name}""" -filter:v scale="-2:720" -b:v 2500k -c:a copy """{out}""" -y'
    try:
        await ffmpeg_progress(cmd, name, progress, FT, edit, ps_name, log=log)
    except Exception as e:
        await log.delete()
        await LOG_END(event, log_end_text)
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
    text = f'**{_ps}D by** : @{BOT_UN}'
    UT = time.time()
    await log.edit("Uploading file")
    if 'x-matroska' in mime:
        try:
            uploader = await fast_upload(f'{out2}', f'{out2}', UT, Drone, edit, '**UPLOADING:**')
            await Drone.send_file(event.chat_id, uploader, caption=text, thumb=JPG, force_document=True)
        except Exception as e:
            await log.delete()
            await LOG_END(event, log_end_text)
            os.rmdir("encodemedia")
            print(e)
            return await edit.edit(f"An error occured while uploading.\n\nContact [SUPPORT]({SUPPORT_LINK})", link_preview=False)
    elif 'webm' in mime:
        try:
            uploader = await fast_upload(f'{out2}', f'{out2}', UT, Drone, edit, '**UPLOADING:**')
            await Drone.send_file(event.chat_id, uploader, caption=text, thumb=JPG, force_document=True)
        except Exception as e:
            await log.delete()
            await LOG_END(event, log_end_text)
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
                await log.delete()
                await LOG_END(event, log_end_text)
                os.rmdir("encodemedia")
                print(e)
                return await edit.edit(f"An error occured while uploading.\n\nContact [SUPPORT]({SUPPORT_LINK})", link_preview=False)
    await edit.delete()
    os.remove(name)
    os.remove(out2)
    await log.delete()
    log_end_text2 = f'**{_ps} PROCESS FINISHED**\n\nTime Taken: {round((time.time()-DT)/60)} minutes\nInitial size: {i_size/1000000}mb.\nFinal size: {f_size/1000000}mb.\n\n[Bot is free now.]({SUPPORT_LINK})'
    await LOG_END(event, log_end_text2)
    
