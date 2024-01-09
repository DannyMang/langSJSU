import os
from dotenv import load_dotenv
from motor.motor_asyncio import AsyncIOMotorClient

load_dotenv()

class Mongo:
    DATABASE_NAME = os.environ["MONGO_DB_DATABASE"]

    def __init__(self):
        self.client = AsyncIOMotorClient(os.environ["MONGO_DB_URL"])
        self.db = self.client[self.DATABASE_NAME]

    async def get_collection(self, collection_name: str):
        """Retrieves an existing collection."""
        return self.db[collection_name]

    async def close(self):
        """Closes the MongoDB connection."""
        await self.client.close()
