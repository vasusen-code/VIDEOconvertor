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

import os, time, requests
from datetime import datetime as dt
from .. import Drone, BOT_UN, MONGODB_URI

from pyrogram import Client
from telethon import events

from ethon.pyutils import rename, file_extension
from ethon.pyfunc import video_metadata

from LOCAL.localisation import SUPPORT_LINK
from main.Database.database import Database
from main.plugins.stuff import download, upload
from LOCAL.localisation import JPG3 as t

async def media_rename(event, msg, new_name):
    edit = await event.client.send_message(event.chat_id, 'Trying to process.', reply_to=msg.id)
    db = Database(MONGODB_URI, 'videoconvertor')
    T = await db.get_thumb(event.sender_id)
    if T is not None:
        ext = T.split("/")[4]
        r = requests.get(T, allow_redirects=True)
        path = dt.now().isoformat("_", "seconds") + ext
        open(path , 'wb').write(r.content)
        THUMB = path
    else:
        THUMB = t
    Drone = event.client
    try:  
        name = await download(msg, edit)
        print(name)
    except Exception as e:
        await edit.edit(f"An error occured while downloading.\n\nContact [SUPPORT]({SUPPORT_LINK})", link_preview=False)
        print(e)
        return
    await edit.edit("Renaming.")
    try:
        out = new_name + file_extension(name)
        rename(name, out)
    except Exception as e:
        await edit.edit(f"An error occured while renaming.\n\nContact [SUPPORT]({SUPPORT_LINK})", link_preview=False)
        print(e)
        return
    try:
        caption = None
        if msg.text:
            caption = msg.text
        await upload(out, edit, thumb=THUMB, caption=caption)
    except Exception as e:
        await edit.edit(f"An error occured while uploading.\n\nContact [SUPPORT]({SUPPORT_LINK})", link_preview=False)
        print(e)
        return
    await edit.delete()
    os.remove(out)
