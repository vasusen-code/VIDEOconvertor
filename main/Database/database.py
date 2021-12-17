#Tg:ChauhanMahesh/DroneBots
#Github.com/vasusen-code

import datetime
import motor.motor_asyncio
from .. import MONGODB_URI

SESSION_NAME = 'videoconvertor'

class Database:
  
    def __init__(self, MONGODB_URI, SESSION_NAME):
        self._client = motor.motor_asyncio.AsyncIOMotorClient(MONGODB_URI)
        self.db = self._client[SESSION_NAME]
        self.col = self.db.users
        self.ban = self.db.niggas
        
    def new_user(self, id):
        return dict(id=id , ban_status=dict(is_banned=False))
           
    async def add_user(self,id):
        user = self.new_user(id)
        await self.col.insert_one(user)
      
    async def is_user_exist(self, id):
        user = await self.col.find_one({'id':int(id)})
        return True if user else False

    async def total_users_count(self):
        count = await self.col.count_documents({})
        return count

    def ban_user(self, id):
        return dict(banned=id)
      
    async def banning(self, id):
        ban = self.ban_user(id)
        await self.ban.insert_one(ban)
        
    async def is_banned(self, id):
        banned = await self.ban.find_one({'banned': int(id)})
        return True if banned else False
      
    async def unbanning(self, id):
        await self.ban.delete_many({'banned': int(id)})
    
    async def get_users(self):
        users = self.col.find({})
        return users
    
    async def limit_user(self, id):
        DT = datetime.date.today().isoformat()
        limit = dict(limited_on=DT)
        await self.col.update_one({'id': id}, {'$set': {'limit': limit}})
    
    async def get_limit(self, id):
        user = await self.col.find_one({'id':int(id)})
        DT = datetime.date.today().isoformat()
        default = dict(limited_on=DT)
        return user.get('limit', default)
    
