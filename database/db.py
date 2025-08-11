import motor.motor_asyncio
from config import DB_NAME, DB_URI

class Database:

    def __init__(self, uri, database_name):
        self._client = motor.motor_asyncio.AsyncIOMotorClient(uri)
        self.db = self._client[database_name]
        self.col = self.db.users
        self.sess_col = self.db.session
        self.sub_col = self.db.subscriptions

    def new_user(self, id, name):
        return dict(
            id = id,
            name = name,
            session = None,
        )

    async def add_user(self, user_id, name):
        user = {"user_id": user_id, "name": name}
        await self.col.insert_one(user)

    async def remove_user(self, user_id):
        await self.col.delete_one({"user_id": user_id})

    async def total_users_count(self):
        count = await self.col.count_documents({})
        return count

    async def is_user_exist(self, user_id):
        user = await self.col.find_one({"user_id": user_id})
        return bool(user)

    async def get_all_users(self):
        return self.col.find({})

    async def delete_user(self, user_id):
        await self.col.delete_many({"user_id": user_id})

    async def get_session(self, user_id):
        data = await self.sess_col.find_one({"user_id": user_id})
        return data.get("session") if data else None

    async def set_session(self, user_id, session):
        await self.sess_col.update_one(
            {"user_id": user_id},
            {"$set": {"session": session}},
            upsert=True
        )

    async def get_user_subscription(self, user_id):
        data = await self.sub_col.find_one({"user_id": user_id})
        return data.get("subscription") if data else None

    async def set_user_subscription(self, user_id, subscription_data):
        await self.sub_col.update_one(
            {"user_id": user_id},
            {"$set": {"subscription": subscription_data}},
            upsert=True
        )

db = Database(DB_URI, DB_NAME)
