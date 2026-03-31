# atlas/adapters/graph/neo4j_adapter.py

from .base_graph import GraphAdapter

class Neo4jAdapter(GraphAdapter):
    def __init__(self, driver):
        self.driver = driver

    async def add_edge(self, a, relation, b):
        query = """
        MERGE (x {id: $a})
        MERGE (y {id: $b})
        MERGE (x)-[:REL {type: $rel}]->(y)
        """
        with self.driver.session() as session:
            session.run(query, a=a, b=b, rel=relation)

    async def neighbors(self, node):
        query = """
        MATCH (x {id: $id})-[r]->(y)
        RETURN y.id, r.type
        """
        with self.driver.session() as session:
            result = session.run(query, id=node)
            return [(r["y.id"], r["r.type"]) for r in result]
