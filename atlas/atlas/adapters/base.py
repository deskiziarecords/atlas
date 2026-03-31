class StorageAdapter:
    async def insert(self, obj):
        raise NotImplementedError

    async def query(self, query):
        raise NotImplementedError

    async def update(self, id, obj):
        raise NotImplementedError

    async def delete(self, id):
        raise NotImplementedError
