#Tg:ChauhanMahesh/Dronebots
#Github.com/vasusen-code

import os
from .. import Drone 
from telethon import events, Button
from main.plugins.rename import media_rename
from main.plugins.compressor import compress
from main.plugins.convertor import mp3, flac

@Drone.on(events.NewMessage(incoming=True,func=lambda e: e.is_private))
async def compin(event):
    if event.is_private:
        media = event.media
        if media:
            video = event.file.mime_type
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
                                [Button.inline("RENAME", data="rename")]])

@Drone.on(events.callbackquery.CallbackQuery(data="convert"))
async def convert(event):
    buttons=[
        [Button.inline("MP3", data="mp3"),
         Button.inline("FLAC", data="flac"),
         Button.inline("WAV", data="wav")],
        [Button.inline("MP4", data="mp4"),
         Button.inline("WEBM", data="webm"),
         Button.inline("MKV", data="mkv")],
        [Button.inline("FILE", data="file"),
         Button.inline("VIDEO", data="video")]])
    
#-----------------------------------------------------------------------------------------

@Drone.on(events.callbackquery.CallbackQuery(data="mp3"))
async def vtmp3(event):
    button = await event.get_message()
    msg = await button.get_reply_message()  
    await event.delete()
    if not os.path.isdir("audioconvert"):
        await event.delete()
        os.mkdir("audioconvert")
        await mp3(event, msg)
        os.rmdir("audioconvert")
    else:
        await event.edit("Another process in progress!")
        
@Drone.on(events.callbackquery.CallbackQuery(data="mp3"))
async def vtmp3(event):
    button = await event.get_message()
    msg = await button.get_reply_message()  
    await event.delete()
    if not os.path.isdir("audioconvert"):
        await event.delete()
        os.mkdir("audioconvert")
        await flac(event, msg)
        os.rmdir("audioconvert")
    else:
        await event.edit("Another process in progress!")

@Drone.on(events.callbackquery.CallbackQuery(data="rename"))
async def rename(event):                            
    button = await event.get_message()
    msg = await button.get_reply_message()  
    await event.delete()
    async with Drone.conversation(event.chat_id) as conv: 
        cm = await conv.send_message("Send me a new name for the file as a `reply` to this message.\n\n**NOTE:** `.ext` is not required.")                              
        try:
            m = await conv.get_reply()
            new_name = m.text
            await cm.delete()                    
            if not m:                
                return await cm.edit("No response found.")
        except Exception as e: 
            print(e)
            return await cm.edit("An error occured while waiting for the response.")
    await media_rename(event, msg, new_name)                     
                   
@Drone.on(events.callbackquery.CallbackQuery(data="compress"))
async def compresss(event):
    button = await event.get_message()
    msg = await button.get_reply_message()  
    if not os.path.isdir("compressmedia"):
        await event.delete()
        os.mkdir("compressmedia")
        await compress(event, msg)
        os.rmdir("compressmedia")
    else:
        await event.edit("Another process in progress!")
    
