#Tg:ChauhanMahesh/Dronebots
#Github.com/vasusen-code

from .. import Drone 
from telethon import events, Button

@Drone.on(events.NewMessage(incoming=True,func=lambda e: e.is_private))
async def compin(event):
    if event.is_private:
        msg = event.message
        media = event.media
        video = event.document.mime_type
        if media:
            if 'video' in video:
            else:
        else:
            return
    
      
