# atlas/adapters/nosql/mongo_adapter.py

from atlas.adapters.base import StorageAdapter

class MongoAdapter(StorageAdapter):
    def __init__(self, client, db_name, collection):
        self.collection = client[db_name][collection]

    async def insert(self, obj):
        self.collection.insert_one(obj)

    async def query(self, query):
        return list(self.collection.find(query))

    async def update(self, id, obj):
        self.collection.update_one({"_id": id}, {"$set": obj})

    async def delete(self, id):
        self.collection.delete_one({"_id": id})
