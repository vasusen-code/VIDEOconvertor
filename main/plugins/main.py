#Tg:ChauhanMahesh/Dronebots
#Github.com/vasusen-code

from .. import Drone 
from telethon import events, Button

@Drone.on(events.NewMessage(incoming=True,func=lambda e: e.is_private))
async def compin(event):
    if event.is_private:
        media = event.media
        video = event.document.mime_type
        if media:
            if 'video' in video:
                await event.reply("📽",
                            buttons=[
                                [Button.inline("COMPRESS", data="compress"),
                                 Button.inline("CONVERT", data="convert")],
                                [Button.inline("RENAME", data="rename"),
                                 Button.inline("TRIM", data="trim")]
                            ])
                
            else:
                await event.reply(,
                            buttons=[  
                                [Button.inline("RENAME", data="rename"),
        else:
            return
    
      
