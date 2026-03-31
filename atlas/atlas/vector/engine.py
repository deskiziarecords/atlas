# atlas/vector/engine.py
class VectorEngine:
    def __init__(self):
        self.spaces = {}

    async def register_space(self, name, index):
        self.spaces[name] = index

    async def search(self, query_vectors):
        results = {}
        for name, vector in query_vectors.items():
            if name in self.spaces:
                results[name] = await self.spaces[name].search(vector)
        return results
