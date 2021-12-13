from .. import Drone
from telethon import events, Button
from LOCAL.localisation import START_TEXT as st
from LOCAL.localisation import JPG as file

@Drone.on(events.NewMessage(incoming=True, pattern="/start"))
async def start(event):
    await event.reply(f'{st}', file=file,
                      buttons=[
                              [Button.inline("Menu.", data="menu")]
                              ])
                      

@Asst.on(events.callbackquery.CallbackQuery(data="plugins"))
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
    
                   
                         
