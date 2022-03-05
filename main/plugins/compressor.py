#  This file is part of the VIDEOconvertor distribution.
#  Copyright (c) 2021 vasusen-code ; All rights reserved. 
#
#  This program is free software: you can redistribute it and/or modify
#  it under the terms of the GNU General Public License as published by
#  the Free Software Foundation, version 3.
#
#  This program is distributed in the hope that it will be useful, but
#  WITHOUT ANY WARRANTY; without even the implied warranty of
#  MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE. See the GNU
#  General Public License for more details.
#
#  License can be found in < https://github.com/vasusen-code/VIDEOconvertor/blob/public/LICENSE> .

from .. import Drone, BOT_UN

import asyncio, time, subprocess, re, os, ffmpeg
from datetime import datetime as dt

from pyrogram import Client

from telethon import events

from ethon.pyfunc import video_metadata

from LOCAL.localisation import SUPPORT_LINK, JPG, JPG2, JPG3
from LOCAL.utils import ffmpeg_progress
from main.plugins.stuff import upload, download

async def compress(event, msg, ffmpeg_cmd=0, ps_name=None):
    if ps_name is None:
        ps_name = '**COMPRESSING:**'
    _ps = "COMPRESS"
    if ps_name != "**COMPRESSING:**":
        _ps = "ENCODE"
    Drone = event.client
    edit = await Drone.send_message(event.chat_id, "Trying to process.", reply_to=msg.id)
    DT = time.time()
    try:
        n = await download(msg, edit) 
    except Exception as e:
        os.rmdir("encodemedia")
        print(e)
        return await edit.edit(f"An error occured while downloading.\n\nContact [SUPPORT]({SUPPORT_LINK})", link_preview=False) 
    name = '__' + dt.now().isoformat("_", "seconds") + ".mp4"
    os.rename(n, name)
    await edit.edit("Extracting metadata...")
    vid = ffmpeg.probe(name)
    codec = vid['streams'][0]['codec_name']
    hgt = video_metadata(name)["height"]
    wdt = video_metadata(name)["width"]
    if ffmpeg_cmd == 2:
        if hgt == 360 or wdt == 640:
            await edit.edit("Fast compress cannot be used for this media, try using HEVC!")
            os.rmdir("encodemedia")
            return
    if ffmpeg_cmd == 3:
        if codec == 'hevc':
            await edit.edit("The given video is already in H.265 codec.")
            os.rmdir("encodemedia")
            return
    if ffmpeg_cmd == 4:
        if codec == 'h264':
            await edit.edit("The given video is already in H.264 codec.")
            os.rmdir("encodemedia")
            return
    out = "compressed_" + dt.now().isoformat("_", "seconds") + ".mp4"
    FT = time.time()
    progress = f"progress-{FT}.txt"
    cmd = f'ffmpeg -hide_banner -loglevel quiet -progress {progress} -i """{name}""" None """{out}""" -y'
    if ffmpeg_cmd == 1:
        cmd = f'ffmpeg -hide_banner -loglevel quiet -progress {progress} -i """{name}""" -preset ultrafast -vcodec libx265 -crf 28 -acodec copy """{out}""" -y'
    elif ffmpeg_cmd == 2:
        cmd = f'ffmpeg -hide_banner -loglevel quiet -progress {progress} -i """{name}""" -c:v libx265 -crf 22 -preset ultrafast -s 640x360 -c:a copy """{out}""" -y'
    elif ffmpeg_cmd == 3:
        cmd = f'ffmpeg -hide_banner -loglevel quiet -progress {progress} -i """{name}""" -preset ultrafast -vcodec libx265 -crf 18 -acodec copy """{out}""" -y'
    elif ffmpeg_cmd == 4:
        cmd = f'ffmpeg -hide_banner -loglevel quiet -progress {progress} -i """{name}""" -preset ultrafast -vcodec libx264 -crf 18 -acodec copy """{out}""" -y'
    try:
        await ffmpeg_progress(cmd, name, progress, FT, edit, ps_name, log=log)
    except Exception as e:
        os.rmdir("encodemedia")
        print(e)
        return await edit.edit(f"An error occured while FFMPEG progress.\n\nContact [SUPPORT]({SUPPORT_LINK})", link_preview=False)
    out2 = "_" + n
    os.rename(out, out2)
    i_size = os.path.getsize(name)
    f_size = os.path.getsize(out2)
    text = F'**ENCODED by:** @{BOT_UN}'
    if ps_name != "**ENCODING:**":
        text = f'**COMPRESSED by** : @{BOT_UN}\n\nbefore compressing : `{i_size}`\nafter compressing : `{f_size}`'
    try:
        await upload(out2, edit, thumb=JPG, caption=text)
    except Exception as e:
        os.rmdir("encodemedia")
        print(e)
        return await edit.edit(f"An error occured while uploading.\n\nContact [SUPPORT]({SUPPORT_LINK})", link_preview=False)
    await edit.delete()
    os.remove(name)
    os.remove(out2)
    
