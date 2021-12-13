from .. import Drone
from telethon import events, Button
from LOCAL.localisation import START_TEXT as st
from LOCAL.localisation import JPG as file
from LOCAL.localisation import info_text, spam_notice, help_text, DEV

@Drone.on(events.NewMessage(incoming=True, pattern="/start"))
async def start(event):
    await event.reply(f'{st}', file=file,
                      buttons=[
                              [Button.inline("Menu.", data="menu")]
                              ])
                      

@Drone.on(events.callbackquery.CallbackQuery(data="menu"))
async def menu(event):
    await event.edit("",
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
    await event.edit(f'**INFO:**\n\n{info_text}',
                    buttons=[[
                         Button.inline("Menu.", data="menu")]])
    
@Drone.on(events.callbackquery.CallbackQuery(data="notice"))
async def notice(event):
    await event.answer(f'{notice_text}', alert=True)
    
@Drone.on(events.callbackquery.CallbackQuery(data="premium"))
async def premium(event):
    await event.answer('You can purchase a package of 70Rs(aprx 1$) per month for renting a bot on heroku, hence no restrictions for usage.' alert=True)
    
    
