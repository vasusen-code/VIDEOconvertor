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

from .. import Drone, PyroBot
from .. import LIBRARY as telethon

import math, os, time, json
from datetime import datetime as dt
from decouple import config

from pyrogram import Client

from telethon import events
from telethon.tl.types import DocumentAttributeVideo

from ethon.telefunc import fast_upload, fast_download
from ethon.pyfunc import video_metadata

def dl_name(mime):
    name = None
    if 'mp4' in mime:
        name = "media_" + dt.now().isoformat("_", "seconds") + ".mp4"
        return name
    elif msg.video:
        name = "media_" + dt.now().isoformat("_", "seconds") + ".mp4"
        return name
    elif 'x-matroska' in mime:
        name = "media_" + dt.now().isoformat("_", "seconds") + ".mkv" 
        return name            
    elif 'webm' in mime:
        name = "media_" + dt.now().isoformat("_", "seconds") + ".webm" 
        return name
    elif 'zip' in mime:
        name = "media_" + dt.now().isoformat("_", "seconds") + ".zip" 
        return name            
    elif 'jpg' in mime:
        name = "media_" + dt.now().isoformat("_", "seconds") + ".jpg" 
        return name
    elif 'png' in mime:
        name = "media_" + dt.now().isoformat("_", "seconds") + ".png"
        return name
    elif 'pdf' in mime:
        name = "media_" + dt.now().isoformat("_", "seconds") + ".pdf" 
        return name
    elif 'rar' in mime:
        name = "media_" + dt.now().isoformat("_", "seconds") + ".rar"
        return name
    elif 'mp3' in mime:
        name = "media_" + dt.now().isoformat("_", "seconds") + ".mp3" 
        return name
    elif 'ogg' in mime:
        name = "media_" + dt.now().isoformat("_", "seconds") + ".ogg" 
        return name          
    elif 'flac' in mime:
        name = "media_" + dt.now().isoformat("_", "seconds") + ".flac"  
        return name
    elif 'wav' in mime:
        name = "media_" + dt.now().isoformat("_", "seconds") + ".wav" 
        return name
    elif 'webp' in mime:
        name = "media_" + dt.now().isoformat("_", "seconds") + ".webp" 
        return name
    
FINISHED_PROGRESS_STR = "█"
UN_FINISHED_PROGRESS_STR = ""
DOWNLOAD_LOCATION = "./"

async def PFP(
    current,
    total,
    bot,
    ud_type,
    message,
    start
):
    now = time.time()
    diff = now - start
    if round(diff % 10.00) == 0 or current == total:
        percentage = current * 100 / total
        status = DOWNLOAD_LOCATION + "/status.json"
        if os.path.exists(status):
            with open(status, 'r+') as f:
                statusMsg = json.load(f)
                if not statusMsg["running"]:
                    bot.stop_transmission()
        speed = current / diff
        elapsed_time = round(diff) * 1000
        time_to_completion = round((total - current) / speed) * 1000
        estimated_total_time = elapsed_time + time_to_completion

        elapsed_time = TimeFormatter(milliseconds=elapsed_time)
        estimated_total_time = TimeFormatter(milliseconds=estimated_total_time)

        progress = "**[{0}{1}]** `| {2}%`\n\n".format(
            ''.join([FINISHED_PROGRESS_STR for i in range(math.floor(percentage / 10))]),
            ''.join([UN_FINISHED_PROGRESS_STR for i in range(10 - math.floor(percentage / 10))]),
            round(percentage, 2))

        tmp = progress + "GROSSS: {0} of {1}\n\nSpeed: {2}/s\n\nETA: {3}\n".format(
            humanbytes(current),
            humanbytes(total),
            humanbytes(speed),
            estimated_total_time if estimated_total_time != '' else "0 s"
        )
        try:
            if not message.photo:
                await message.edit_text(
                    text="{}\n {}".format(
                        ud_type,
                        tmp
                    )
                )
            else:
                await message.edit_caption(
                    caption="{}\n {}".format(
                        ud_type,
                        tmp
                    )
                )
        except:
            pass

def humanbytes(size):
    if not size:
        return ""
    power = 2**10
    n = 0
    Dic_powerN = {0: ' ', 1: 'Ki', 2: 'Mi', 3: 'Gi', 4: 'Ti'}
    while size > power:
        size /= power
        n += 1
    return str(round(size, 2)) + " " + Dic_powerN[n] + 'B'

def TimeFormatter(milliseconds: int) -> str:
    seconds, milliseconds = divmod(int(milliseconds), 1000)
    minutes, seconds = divmod(seconds, 60)
    hours, minutes = divmod(minutes, 60)
    days, hours = divmod(hours, 24)
    tmp = ((str(days) + "d, ") if days else "") + \
        ((str(hours) + "h, ") if hours else "") + \
        ((str(minutes) + "m, ") if minutes else "") + \
        ((str(seconds) + "s, ") if seconds else "")
    return tmp[:-2]

async def download(msg, reply):
    if telethon != "TELETHON":
        reply = await PyroBot.edit_message_text(msg.sender_id, reply.id, 'Preparing to download.')
        msg = await PyroBot.get_messages(msg.sender_id, msg.id)
        file = await PyroBot.download_media(
            msg,
            progress=PFP,
            progress_args=(
                PyroBot,
                "**DOWNLOADING:**\n",
                reply,
                time.time()
            )
        )
        return file
    else:
        name = msg.file.name
        if name is None:
            name = dl_name(msg.file.mime_type)
        media = msg.media
        if hasattr(msg.media, "document"):
            media = msg.media.document
        await fast_download("./" + name, media, Drone, reply, time.time(), "**DOWNLOADING:**")
        return "./" + name
    
async def upload(file, edit, caption=None, thumb=None):
    if telethon != "TELETHON":
        edit = await PyroBot.edit_message_text(edit.chat_id, edit.id, 'Starting Upload.')
        if str(file).split(".")[-1] in ['mkv', 'mp4', 'webm']:
            if str(file).split(".")[-1] in ['webm', 'mkv']:
                path = str(file).split(".")[0] + ".mp4"
                os.rename(file, path) 
                file = str(file).split(".")[0] + ".mp4"
            data = video_metadata(file)
            duration = data["duration"]
            await PyroBot.send_video(
                chat_id=edit.chat.id,
                video=file,
                caption=caption,
                supports_streaming=True,
                duration=duration,
                thumb=thumb,
                progress=PFP,
                progress_args=(
                    PyroBot,
                    '**UPLOADING:**\n',
                    edit,
                    time.time()
                )
            )
        elif str(file).split(".")[-1] in ['jpg', 'jpeg', 'png', 'webp']:
            await edit.edit("Uploading photo.")
            await PyroBot.send_file(edit.chat.id, file, caption=caption)
        else:
            await PyroBot.send_document(
                edit.chat.id,
                file, 
                caption=caption,
                thumb=thumb,
                progress=PFP,
                progress_args=(
                    PyroBot,
                    '**UPLOADING:**\n',
                    edit,
                    time.time()
                )
            )
    else:
        if str(file).split(".")[-1] in ['mp4', 'mkv']:
            metadata = video_metadata(file)
            width = metadata["width"]
            height = metadata["height"]
            duration = metadata["duration"]
            attributes = [DocumentAttributeVideo(duration=duration, w=width, h=height, supports_streaming=True)]
            parallel = await fast_upload(
                file, 
                file, 
                time.time(),
                Drone, 
                edit, 
                '**UPLOADING:**'
            )
            await Drone.send_file(
                edit.chat_id, 
                parallel, 
                caption=caption,
                thumb=thumb,
                attributes=attributes, 
                force_document=False
            )  
        else:
            parallel = await fast_upload(
                file,
                file, 
                time.time(),
                Drone, 
                edit, 
                '**UPLOADING:**'
            )
            await Drone.send_file(
                edit.chat_id, 
                parallel, 
                caption=caption, 
                thumb=thumb, 
                force_document=True
            )  
     
            
           
            
        






