import os
from dotenv import load_dotenv
from pymongo import MongoClient


load_dotenv()

class Mongo():
    def __init__(self):
        """initialize  connection """
        mongo_uri =  os.environ["MONGO_DB_URL"]
        self.client = MongoClient(mongo_uri)
        self.db = self.client["your_database_name"]

    def __del__(self):
        # Close the connection on object deletion
        self.client.close()
