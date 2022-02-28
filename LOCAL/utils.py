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

import time, math, re, asyncio, subprocess
from ethon.pyfunc import total_frames as tf
from telethon import events

def time_formatter(milliseconds: int) -> str:
    """Inputs time in milliseconds, to get beautified time,
    as string"""
    seconds, milliseconds = divmod(int(milliseconds), 1000)
    minutes, seconds = divmod(seconds, 60)
    hours, minutes = divmod(minutes, 60)
    days, hours = divmod(hours, 24)
    weeks, days = divmod(days, 7)
    tmp = (
        ((str(weeks) + "w:") if weeks else "")
        + ((str(days) + "d:") if days else "")
        + ((str(hours) + "h:") if hours else "")
        + ((str(minutes) + "m:") if minutes else "")
        + ((str(seconds) + "s:") if seconds else "")
    )
    if tmp.endswith(":"):
        return tmp[:-1]
    else:
        return tmp
 
def humanbytes(size):
    if size in [None, ""]:
        return "0 B"
    for unit in ["B", "KB", "MB", "GB", "TB", "PB", "EB", "ZB", "YB"]:
        if size < 1024:
            break
        size /= 1024
    return f"{size:.2f} {unit}"
   
async def ffmpeg_progress(cmd, file, progress, now, event, ps_name, log=None):
    total_frames = tf(file)
    with open(progress, "w") as fk:
        pass
    proce = await asyncio.create_subprocess_shell(cmd, stdout=asyncio.subprocess.PIPE, stderr=asyncio.subprocess.PIPE)
    while proce.returncode != 0:
        await asyncio.sleep(3)
        with open(progress, "r+") as fil:
            text = fil.read()
            frames = re.findall("frame=(\\d+)", text)
            size = re.findall("total_size=(\\d+)", text)
            speed = 0
            if len(frames):
                elapse = int(frames[-1])
            if len(size):
                size = int(size[-1])
                per = elapse * 100 / int(total_frames)
                time_diff = time.time() - int(now)
                speed = round(elapse / time_diff, 2)
            if int(speed) != 0:
                some_eta = ((int(total_frames) - elapse) / speed) * 1000
                progress_str = "**[{0}{1}]** `| {2}%\n\n`".format(
                    "".join("█" for i in range(math.floor(per / 5))),
                    "".join("" for i in range(20 - math.floor(per / 5))),
                    round(per, 2),
                )
                e_size = humanbytes(size) + " of ~" + humanbytes((size / per) * 100)
                eta = time_formatter(some_eta)
                await event.edit(f'{ps_name}\n\n{progress_str}' + f'GROSS: {e_size}\n\nETA: {eta}')
                if log != None:
                    await log.edit(f'{ps_name}\n\n{progress_str}' + f'GROSS: {e_size}\n\nETA: {eta}')
