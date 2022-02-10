#Tg:ChauhanMahesh/Dronebots
#Github.com/vasusen-code

import os
from .. import Drone 
from telethon import events, Button
from main.plugins.rename import media_rename
from main.plugins.compressor import compress
from main.plugins.trimmer import trim
from main.plugins.convertor import mp3, flac, wav, mp4, mkv, webm, file, video
from main.plugins.encoder import encode

@Drone.on(events.NewMessage(incoming=True,func=lambda e: e.is_private))
async def compin(event):
    if event.is_private:
        media = event.media
        if media:
            video = event.file.mime_type
            if 'video' in video or event.video:
                async with Drone.conversation(event.chat_id) as conv:
                    try:
                        buttons = [
                            [Button.text("ENCODE", resize=True, single_use=True)], 
                            [Button.text("COMPRESS", resize=True, single_use=True),
                             Button.text("CONVERT", resize=True, single_use=True)],
                            [Button.text("RENAME", resize=True, single_use=True),
                             Button.text("TRIM", resize=True, single_use=True)]])
                        await conv.send_message("📽",
                                                buttons=buttons)
                        response = await conv.get_response()
                        await respond(event, conv, response)
                    except Exception as e:
                        print(e)
                        await conv.send_message("Cannot wait more longer for your response!")
                        return
            elif 'png' in video:
                return
            elif 'jpeg' in video:
                return
            elif 'jpg' in video:
                return    
            else:
                async with Drone.conversation(event.chat_id) as conv:
                    try:
                        await conv.send_message('📦', buttons=[[Button.text('RENAME', resize=True, single_use=True)]])
                        response = await conv.get_response()
                        await respond(event, conv, response)
                    except Exception as e:
                        print(e)
                        await conv.send_message("Cannot wait more longer for your response!")
                        return
                 
async def respond(event, conv, response):
    text = response.text
    if text == "COMPRESS":
        await _compress(event, conv) 
    if text == "ENCODE":
        await _encode(event, conv) 
    if text == "RENAME":
        await __rename(event)
    else:
        await conv.send_message("**Invalid response!**")
        
async def _encode(event):
    try: 
        await conv.send_message("🔀**ENCODE into?**",
                                buttons=[
                                    [Button.text("240", resize=True, single_use=True),
                                     Button.text("360", resize=True, single_use=True),
                                     Button.text("480", resize=True, single_use=True),
                                     Button.text("720", resize=True, single_use=True)]
                                    [Button.text("x265", resize=True, single_use=True),
                                     Button.text("x264", resize=True, single_use=True)],
                                    [Button.text("BACK", resize=True, single_use=True)]])
        response = await conv.get_response()
        await __encode(event, response)
    except Exception as e:
        print(e)
        await conv.send_message("Cannot wait more longer for your response!")
        
async def _compress(event, conv):
    try: 
        await conv.send_message("**Your choice of compress?**",
                                buttons=[
                                    [Button.text("HVEC COMPRESS", resize=True, single_use=True)],
                                    [Button.text("FAST COMPRESS", resize=True, single_use=True)]])
        response = await conv.get_response()
        await __compress(event, response) 
    except Exception as e:
        print(e)
        await conv.send_message("Cannot wait more longer for your response!")
        
@Drone.on(events.callbackquery.CallbackQuery(data="convert"))
async def convert(event):
    await event.edit("🔃**CONVERT:**",
                    buttons=[
                        [Button.inline("MP3", data="mp3"),
                         Button.inline("FLAC", data="flac"),
                         Button.inline("WAV", data="wav")],
                        [Button.inline("MP4", data="mp4"),
                         Button.inline("WEBM", data="webm"),
                         Button.inline("MKV", data="mkv")],
                        [Button.inline("FILE", data="file"),
                         Button.inline("VIDEO", data="video")],
                        [Button.inline("BACK", data="back")]])
                        
@Drone.on(events.callbackquery.CallbackQuery(data="back"))
async def back(event):
    await event.edit("📽",
                    buttons=[
                        [Button.inline("ENCODE", data="encode")],
                        [Button.inline("COMPRESS", data="compress"),
                         Button.inline("CONVERT", data="convert")],
                        [Button.inline("RENAME", data="rename"),
                         Button.inline("TRIM", data="trim")]])
                            
#-----------------------------------------------------------------------------------------

@Drone.on(events.callbackquery.CallbackQuery(data="mp3"))
async def vtmp3(event):
    button = await event.get_message()
    msg = await button.get_reply_message() 
    if not os.path.isdir("audioconvert"):
        await event.delete()
        os.mkdir("audioconvert")
        await mp3(event, msg)
        os.rmdir("audioconvert")
    else:
        await event.edit("Another process in progress!")
        
@Drone.on(events.callbackquery.CallbackQuery(data="flac"))
async def vtflac(event):
    button = await event.get_message()
    msg = await button.get_reply_message()  
    if not os.path.isdir("audioconvert"):
        await event.delete()
        os.mkdir("audioconvert")
        await flac(event, msg)
        os.rmdir("audioconvert")
    else:
        await event.edit("Another process in progress!")
        
@Drone.on(events.callbackquery.CallbackQuery(data="wav"))
async def vtwav(event):
    button = await event.get_message()
    msg = await button.get_reply_message() 
    if not os.path.isdir("audioconvert"):
        await event.delete()
        os.mkdir("audioconvert")
        await wav(event, msg)
        os.rmdir("audioconvert")
    else:
        await event.edit("Another process in progress!")
        
@Drone.on(events.callbackquery.CallbackQuery(data="mp4"))
async def vtmp4(event):
    button = await event.get_message()
    msg = await button.get_reply_message() 
    await event.delete()
    await mp4(event, msg)
    
@Drone.on(events.callbackquery.CallbackQuery(data="mkv"))
async def vtmkv(event):
    button = await event.get_message()
    msg = await button.get_reply_message() 
    await event.delete()
    await mkv(event, msg)  
    
@Drone.on(events.callbackquery.CallbackQuery(data="webm"))
async def vtwebm(event):
    button = await event.get_message()
    msg = await button.get_reply_message() 
    await event.delete()
    await webm(event, msg)  
    
@Drone.on(events.callbackquery.CallbackQuery(data="file"))
async def vtfile(event):
    button = await event.get_message()
    msg = await button.get_reply_message() 
    await event.delete()
    await file(event, msg)    

@Drone.on(events.callbackquery.CallbackQuery(data="video"))
async def ftvideo(event):
    button = await event.get_message()
    msg = await button.get_reply_message() 
    await event.delete()
    await video(event, msg)
    
async def __rename(msg):         
    markup = msg.client.build_reply_markup(Button.force_reply())
    async with Drone.conversation(msg.chat_id) as conv: 
        cm = await conv.send_message("Send me a new name for the file as a `reply` to this message.\n\n**NOTE:** `.ext` is not required.", buttons=markup)                              
        try:
            m = await conv.get_reply()
            new_name = m.text
            await cm.delete()                    
        except Exception as e: 
            print(e)
            return await conv.send_message("No response found.")
    await media_rename(msg, msg, new_name)                     
                   
async def hcomp(msg):
    if not os.path.isdir("compressmedia"):
        os.mkdir("compressmedia")
        cmd = '-preset ultrafast -vcodec libx265 -crf 28 -acodec copy'
        await compress(msg, msg, cmd)
        os.rmdir("compressmedia")
    else:
        await msg.send_message(msg.chat_id, "Another process in progress!")

async def fcomp(msg):
    if not os.path.isdir("compressmedia"):
        os.mkdir("compressmedia")
        cmd = '-vf scale=-1:360 -c:v libx265 -crf 16 -preset ultrafast -c:a copy'
        await compress(msg, msg, cmd)
        os.rmdir("compressmedia")
    else:
        await msg.send_message(msg.chat_id, "Another process in progress!")

async def __compress(event, response):
    if response.text == "HVEC COMPRESS":
        await hcomp(event)
    if response.text == "FAST COMPRESS":
        await fcomp(event)
      
async def __encode(msg, response):
    resolutions = ['240', '360', '480', '720']
    libs = ['x264', 'x265']
    text = response.text
    if text in resolutions:
        if not os.path.isdir("encodemedia"):
            os.mkdir("encodemedia")
            await encode(msg, msg, text)
            os.rmdir("encodemedia")
        else:
            await msg.send_message(msg.chat_id, "Another process in progress!")
        
async def __trim(event):                            
    markup = event.client.build_reply_markup(Button.force_reply())
    async with Drone.conversation(event.chat_id) as conv: 
        try:
            xx = await conv.send_message("send me the start time of the video you want to trim from as a reply to this. \n\nIn format hh:mm:ss , for eg: `01:20:69` ", buttons=markup)
            x = await conv.get_reply()
            st = x.text
            await xx.delete()                 
        except Exception as e: 
            print(e)
            return await conv.send_message("No response found.")
        try:
            xy = await conv.send_message("send me the end time of the video you want to trim till as a reply to this.  \n\nIn format hh:mm:ss , for eg: `01:20:69` ", buttons=markup)
            y = await conv.get_reply()
            et = y.text
            await xy.delete()                    
        except Exception as e: 
            print(e)
            return await conv.send_message("No response found.")
        await trim(event, event, st, et)
            
