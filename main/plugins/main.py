#Tg:ChauhanMahesh/Dronebots
#Github.com/vasusen-code

from .. import Drone 
from telethon import events, Button
from main.plugins.rename import media_rename

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
                await event.reply('📦',
                            buttons=[  
                                [Button.inline("RENAME", data="rename"),
        else:
            return
    
      
@Drone.on(events.callbackquery.CallbackQuery(data="rename"))
async def rename(event):
    async with Drone.conversation(id) as conv: 
        await conv.send_message("Send me a new name for the file as a `reply` to this message.\n\n**NOTE:** `.ext` is not required.")
        m = await conv.get_reply()
        name = m.text
        asyncio.sleep(60)                        
        if not m:
            await event.                   
