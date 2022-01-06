
#tg:chauhanMahesh/DroneBots
#github.com/vasusen-code

import heroku3 
from .. import Drone, AUTH_USERS, ACCESS_CHANNEL, MONGODB_URI
from telethon import events , Button
from decouple import config
from main.Database.database import Database
from telethon.errors.rpcerrorlist import UserNotParticipantError
from telethon.tl.functions.channels import GetParticipantRequest
from telegraph import upload_file
from telethon.errors.rpcerrorlist import FloodWaitError

def mention(name, id):
    return f'[{name}](tg://user?id={id})'

#Forcesub-----------------------------------------------------------------------------------

async def force_sub(id):
    FORCESUB = config("FORCESUB", default=None)
    if not str(FORCESUB).startswith("-100"):
        FORCESUB = int("-100" + str(FORCESUB))
    ok = False
    try:
        x = await Drone(GetParticipantRequest(channel=int(FORCESUB), participant=int(id)))
        left = x.stringify()
        if 'left' in left:
            ok = True
        else:
            ok = False
    except UserNotParticipantError:
        ok = True 
    return ok

#Thumbnail--------------------------------------------------------------------------------------------------------------

async def set_thumbnail(event, img):
    edit = await event.client.send_message(event.chat_id, 'Trying to process.')
    try:
        path = await event.client.download_media(img)
        meta = upload_file(path)
        link = f'https://telegra.ph{meta[0]}'
    except Exception as e:
        print(e)
        return await edit.edit("Failed to Upload on Tgraph.")
    await db.update_thumb_link(event.sender_id, link)
    await edit.edit("Done!")
    
async def rem_thumbnail(event):
    edit = await event.client.send_message(event.chat_id, 'Trying.')
    T = await db.get_thumb(event.sender_id)
    if T is None:
        return await edit.edit('No thumbnail saved!')
    await db.rem_thumb_link(event.sender_id)
    await edit.edit('Removed!')
    
#Heroku--------------------------------------------------------------------------------------------------------------
   
async def heroku_restart():
    HEROKU_API = config("HEROKU_API", default=None)
    HEROKU_APP_NAME = config("HEROKU_APP_NAME", default=None)
    x = None
    if not HEROKU_API and HEROKU_APP_NAME:
        x = None
    else:
        try:
            acc = heroku3.from_key(HEROKU_API)
            bot = acc.apps()[HEROKU_APP_NAME]
            bot.restart()
            x = True
        except Exception as e:
            print(e)
            x = False
    return x
    
