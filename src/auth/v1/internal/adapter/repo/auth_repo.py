from pymongo import MongoClient
from bson import ObjectId

class AuthRepo():
    def __init__(self, mongo_config):
        self.mongo = None
        self._load_mongo(mongo_config)
    
    def find_user(self, email: str):
        collection = self.db.users

        result = collection.find_one({"email": email})
        return result

    def insert_user(self, user) -> ObjectId:
        collection = self.db.users
        result = collection.insert_one(user)

        return result.inserted_id
    
    def _load_mongo(self, mongo_config):
        client = MongoClient(mongo_config['uri'])
        self.db = client[mongo_config['db_name']]