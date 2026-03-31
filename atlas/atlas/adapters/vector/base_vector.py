# atlas/adapters/vector/base_vector.py

class VectorAdapter:
    async def add(self, id, vector):
        raise NotImplementedError

    async def search(self, vector, top_k=10):
        raise NotImplementedError

    async def delete(self, id):
        raise NotImplementedError
