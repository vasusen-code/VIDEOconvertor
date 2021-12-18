from .. import Drone, ACCESS_CHANNEL
from telethon import events, Button
from LOCAL.localisation import START_TEXT as st
from LOCAL.localisation import JPG as file
from LOCAL.localisation import JPG4
from LOCAL.localisation import info_text, spam_notice, help_text, DEV, premium_text, SUPPORT_LINK
from ethon.teleutils import mention

@Drone.on(events.NewMessage(incoming=True, pattern="/start"))
async def start(event):
    await event.reply(f'{st}', file=file,
                      buttons=[
                              [Button.inline("Menu.", data="menu")]
                              ])
    tag = f'[{event.sender.first_name}](tg://user?id={event.sender_id})'
    await Drone.send_message(int(ACCESS_CHANNEL), f'{tag} started the BOT')
    
@Drone.on(events.callbackquery.CallbackQuery(data="menu"))
async def menu(event):
    await event.edit("**📑MENU.**",
                    buttons=[[
                         Button.inline("info.", data="info"),
                         Button.inline("NOTICE", data="notice")],
                         [
                         Button.inline("PREMIUM", data="premium"),
                         Button.inline("Help.", data="help")],
                         [
                         Button.url("DEVELOPER", url=f"{DEV}")]])
    
@Drone.on(events.callbackquery.CallbackQuery(data="info"))
async def info(event):
    await event.edit(f'**ℹ️NFO:**\n\n{info_text}', file=JPG4,
                    buttons=[[
                         Button.inline("Menu.", data="menu2")]])
    
@Drone.on(events.callbackquery.CallbackQuery(data="menu2"))
async def menu2(event):
    await event.edit("**📑MENU.**", file=file,
                    buttons=[[
                         Button.inline("info.", data="info"),
                         Button.inline("NOTICE", data="notice")],
                         [
                         Button.inline("PREMIUM", data="premium"),
                         Button.inline("Help.", data="help")],
                         [
                         Button.url("DEVELOPER", url=f"{DEV}")]])
    
@Drone.on(events.callbackquery.CallbackQuery(data="notice"))
async def notice(event):
    await event.answer(f'{spam_notice}', alert=True)
    
@Drone.on(events.callbackquery.CallbackQuery(data="premium"))
async def premium(event):
    await event.answer(f'{premium_text}', alert=True)
    
    
@Drone.on(events.callbackquery.CallbackQuery(data="help"))
async def help(event):
    await event.edit('**👥HELP.**',
                    buttons=[[
                         Button.inline("PLUGINS.", data="plugins"),
                         Button.url("SUPPORT.", url=f"{SUPPORT_LINK}")],
                         [
                         Button.inline("Menu.", data="menu")]])
    
@Drone.on(events.callbackquery.CallbackQuery(data="plugins"))
async def plugins(event):
    await event.edit(f'{help_text}',
                    buttons=[[
                         Button.inline("Menu.", data="menu")]])
    
    
    
    
    
