#tg:ChauhanMahesh/DroneBots
#github.com/vasusen-code

from .. import Drone, ACCESS_CHANNEL, AUTH_USERS
from telethon import events, Button
from LOCAL.localisation import START_TEXT as st
from LOCAL.localisation import JPG0 as file
from LOCAL.localisation import JPG4
from LOCAL.localisation import info_text, spam_notice, help_text, DEV, source_text, SUPPORT_LINK
from ethon.teleutils import mention
from main.plugins.actions import set_thumbnail, rem_thumbnail, heroku_restart

@Drone.on(events.NewMessage(incoming=True, pattern="/start"))
async def start(event):
    await event.reply(f'{st}', 
                      buttons=[
                              [Button.inline("Menu.", data="menu")]
                              ])
    tag = f'[{event.sender.first_name}](tg://user?id={event.sender_id})'
    await Drone.send_message(int(ACCESS_CHANNEL), f'{tag} started the BOT')
    
@Drone.on(events.callbackquery.CallbackQuery(data="menu"))
async def menu(event):
    await event.client.send_file(event.chat_id, caption="**📑MENU.**", file=file,
                    buttons=[[
                         Button.inline("info.", data="info"),
                         Button.inline("SOURCE-CODE", data="source")],
                         [
                         Button.inline("NOTICE.", data="notice"),
                         Button.inline("Help/SETTINGS.", data="help")],
                         [
                         Button.url("DEVELOPER", url=f"{DEV}")]])
    await event.delete()
    
@Drone.on(events.callbackquery.CallbackQuery(data="menu2"))
async def menu2(event):
    await event.edit("**📑MENU.**",
                    buttons=[[
                         Button.inline("info.", data="info"),
                         Button.inline("SOURCE-CODE", data="source")],
                         [
                         Button.inline("NOTICE.", data="notice"),
                         Button.inline("Help/SETTINGS.", data="help")],
                         [
                         Button.url("DEVELOPER", url=f"{DEV}")]])
       
@Drone.on(events.callbackquery.CallbackQuery(data="info"))
async def info(event):
    await event.edit(f'**ℹ️NFO:**\n\n{info_text}',
                    buttons=[[
                         Button.inline("Menu.", data="menu2")]])
    
@Drone.on(events.callbackquery.CallbackQuery(data="notice"))
async def notice(event):
    await event.answer(f'{spam_notice}', alert=True)
    
@Drone.on(events.callbackquery.CallbackQuery(data="source"))
async def source(event):
    await event.edit(source_text,
                    buttons=[[
                         Button.url("Main.", url="https://github.com/vasusen-code/videoconvertor/tree/main"),
                         Button.url("PUBLIC", url="https://github.com/vasusen-code/videoconvertor/tree/public")]])
                         
                    
@Drone.on(events.callbackquery.CallbackQuery(data="help"))
async def help(event):
    await event.edit('**👥HELP & SETTINGS.**',
                    buttons=[[
                         Button.inline("set THUMBNAIL.", data="sett"),
                         Button.inline("rem THUMBNAIL.", data='remt')],
                         [
                         Button.inline("PLUGUNS.", data="plugins"),
                         Button.inline("restart", data="restart"),
                         Button.url("SUPPORT.", url=f"{SUPPORT_LINK}")],
                         [
                         Button.inline("Menu.", data="menu2")]])
    
@Drone.on(events.callbackquery.CallbackQuery(data="plugins"))
async def plugins(event):
    await event.edit(f'{help_text}',
                    buttons=[[Button.inline("Menu.", data="menu2")]])
                   
 #-----------------------------------------------------------------------------------------------                            
    
@Drone.on(events.callbackquery.CallbackQuery(data="sett"))
async def sett(event):    
    button = await event.get_message()
    msg = await button.get_reply_message() 
    await event.delete()
    async with Drone.conversation(event.chat_id) as conv: 
        xx = await conv.send_message("Send me any image for thumbnail as a `reply` to this message.")
        x = await conv.get_reply()
        if not x.media:
            xx.edit("No media found.")
        mime = x.file.mime_type
        if not 'png' in mime:
            if not 'jpg' in mime:
                if not 'jpeg' in mime:
                    return await xx.edit("No image found.")
        await set_thumbnail(event, x.media)
        await xx.delete()
        
@Drone.on(events.callbackquery.CallbackQuery(data="remt"))
async def remt(event):  
    await event.delete()
    await rem_thumbnail(event)
    
@Drone.on(events.callbackquery.CallbackQuery(data="restart"))
async def res(event):
    if not f'{event.sender_id}' == f'{int(AUTH_USERS)}':
        return await event.edit("Only authorized user can restart!")
    result = await heroku_restart()
    if result is None:
        await event.edit("You have not filled `HEROKU_API` and `HEROKU_APP_NAME` vars.")
    elif result is False:
        await event.edit("An error occured!")
    elif result is True:
        await event.edit("Restarting app, wait for a minute.")
