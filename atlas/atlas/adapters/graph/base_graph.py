# atlas/adapters/graph/base_graph.py

class GraphAdapter:
    async def add_edge(self, a, relation, b):
        raise NotImplementedError

    async def neighbors(self, node):
        raise NotImplementedError
