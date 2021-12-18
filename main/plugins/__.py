from .. import Drone, AUTH_USERS, ACCESS_CHANNEL, MONGODB_URI
from telethon import events 
import pymongo
from decouple import config
from pymongo import MongoClient
import motor.motor_asyncio
from TelethonBot.Database.mongodb import Database, SESSION_NAME
from ethon.teleutils import mention

#Database command handling--------------------------------------------------------------------------

db = Database(MONGODB_URI, SESSION_NAME)

@Drone.on(events.NewMessage(incoming=True, func=lambda e: e.is_private))
async def incomming(event):
    if not await db.is_user_exist(event.sender_id):
        await db.add_user(event.sender_id)
    await event.forward_to(int(ACCESS_CHANNEL))

async def banned(id):
    await db.get_ban_status(id)
    
@Drone.on(events.NewMessage(incoming=True, from_users=AUTH_USERS , pattern="/users"))
async def listusers(event):
    xx = await event.reply("Counting total users in Database.")
    x = await db.total_users_count()
    await xx.edit(f"Total user(s) {int(x)}")
    
@Drone.on(events.NewMessage(incoming=True, from_users=AUTH_USERS , pattern="^/disallow (.*)" ))
async def bban(event):
    c = event.pattern_match.group(1)
    if not c:
        await event.reply("Disallow who!?")
    if c in AUTH_USERS:
        return await event.reply("I cannot ban an AUTH_USER")
    xx = await db.is_banned(event.sender_id)
    if xx is True:
        return await event.reply("User is already disallowed!")
    else:
        await db.banning(c)
        await event.reply(f"{c} is now disallowed.")
        
@Drone.on(events.NewMessage(incoming=True, from_users=AUTH_USERS , pattern="^/allow (.*)" ))
async def unbban(event):
    xx = event.pattern_match.group(1)
    xy = await db.is_banned(xx)
    if xy is False:
        return await event.reply("User is already allowed!")
    if not xx:
        await event.reply("Allow who?")
    await db.unbanning(xx)
    await event.reply(f"{xx} Allowed! ")
    
#Logging events on tg---------------------------------------------------------------------------------------------

async def LOG_START(event, ps_name):
    chat = config("LOG_CHANNEL", default=None)
    Tag = mention(event.sender_id)
    xx = await event.client.send_message(chat, f'{ps_name} by {Tag}')
    return xx

async def LOG_END(event, ps_name):
    await event.edit(ps_name)
    
#Listing--------------------------------------------------------------------------------------------------------------

def one_trial_queue(id, List1):
    if not f'{id}' in List1:
        List1.append(f'{id}')
    else:
        return False
    
#Not in use
def two_trial_queue(id, List1, List2):
    if not f'{id}' in List1:
        List1.append(f'{id}')
    else:
        if not f'{id}' in List2:
            List2.append(f'{id}')
        else:
            return False

#Not in use        
def ps_queue(id, media, List1, List2):
    List1.append(f'{id}')
    List2.append(media)
    if not len(List1) < 2:
        return 'EMPTY'
    if len(List1) > 2:
        return 'FULL'
