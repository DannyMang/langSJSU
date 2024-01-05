import os
from dotenv import load_dotenv
import redis
from rejson import Client

load_dotenv()

class Redis():
    def __init__(self):
        """initialize  connection """
        self.REDIS_URL = os.environ['REDIS_URL']
        self.REDIS_PASSWORD = os.environ['REDIS_PASSWORD']
        self.REDIS_USER = os.environ['REDIS_USER']
        self.connection_url = f"redis://{self.REDIS_USER}:{self.REDIS_PASSWORD}@{self.REDIS_URL}"

    async def create_connection(self):
        client = redis.Redis.from_url(self.connection_url, db=0)
        return client
    
    def create_rejson_connection(self):
        self.redisJson = Client(host=self.REDIS_HOST,
                                port=self.REDIS_PORT, decode_responses=True, username=self.REDIS_USER, password=self.REDIS_PASSWORD)

        return self.redisJson