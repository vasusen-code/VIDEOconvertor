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

import time, os
from datetime import datetime as dt

from .. import Drone, BOT_UN

from pyrogram import Client

from telethon import events

from ethon.pyfunc import video_metadata, bash
from ethon.pyutils import rename

from LOCAL.localisation import SUPPORT_LINK, JPG, JPG2, JPG3
from main.plugins.stuff import upload, download

async def trim(event, msg, st, et):
    Drone = event.client
    edit = await Drone.send_message(event.chat_id, "Trying to process.", reply_to=msg.id)
    DT = time.time()
    try:
        name = await download(msg, edit) 
    except Exception as e:
        print(e)
        return await edit.edit(f"An error occured while downloading.\n\nContact [SUPPORT]({SUPPORT_LINK})", link_preview=False) 
    try:
        out = "trimmed_" + name
        await edit.edit("Trimming.")
        bash(f'ffmpeg -i {name} -ss {st} -to {et} -acodec copy -vcodec copy {out} -y')
    except Exception as e:
        print(e)
        return await edit.edit(f"An error occured while trimming!\n\nContact [SUPPORT]({SUPPORT_LINK})", link_preview=False)
    text = f"**TRIMMED by :** @{BOT_UN}"
    try:
        await upload(out, edit, thumb=JPG, caption=text) 
    except Exception as e:
        print(e)
        return await edit.edit(f"An error occured while uploading.\n\nContact [SUPPORT]({SUPPORT_LINK})", link_preview=False)
    await edit.delete()
    os.remove(name)
    os.remove(out2)
      
      
      
      
