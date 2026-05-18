import asyncio
from .base import AsyncComponent
from .platinum import PlatinumExtractor
from .neurometal import NeurometalEngine
from ..graph.ferros import FerrosGraph
from ..vector.tungsten import TungstenVector
from ..fusion.synth_fuse import SynthFuseEngine
from ..registry.system import SystemRegistry

class AtlasOrchestrator(AsyncComponent):
    """
    Universal Database Orchestrator (THE "FATHER").
    Coordinate everything: query planning, adapter orchestration, system routing, ingestion pipeline.

    This Orchestrator operates as a standalone service that sub-systems register to
    or are managed by. It maintains the high-level logic and routing.
    """
    def __init__(self):
        self.registry = SystemRegistry()

        # Internal sub-system instances
        self.platinum = PlatinumExtractor()
        self.neurometal = NeurometalEngine()
        self.ferros = FerrosGraph()
        self.tungsten = TungstenVector()
        self.synth_fuse = SynthFuseEngine()

        # Register them
        self.registry.register("platinum", self.platinum)
        self.registry.register("neurometal", self.neurometal)
        self.registry.register("ferros", self.ferros)
        self.registry.register("tungsten", self.tungsten)
        self.registry.register("synth_fuse", self.synth_fuse)

    async def start(self):
        print("ATLAS Orchestrator starting...")
        await self.registry.start_all()

    async def stop(self):
        print("ATLAS Orchestrator stopping...")
        await self.registry.stop_all()

    async def plan_query(self, query):
        """Plans a query across the available sub-systems."""
        print(f"Planning query: {query}")

        # 1. Similarity Search (Tungsten)
        search_results = await self.tungsten.search(query)

        # 2. Dependency & Lineage Traversal (Ferros)
        async def get_context(res):
            graph_context = await self.ferros.traverse(res["id"])
            return {
                "original": res,
                "context": graph_context
            }

        contextual_results = await asyncio.gather(*(get_context(res) for res in search_results))

        # 3. Score Fusion and Ranking (Synth-Fuse)
        fused_results = await self.synth_fuse.fuse_scores(contextual_results)
        ranked_results = await self.synth_fuse.rank(fused_results)

        return {
            "query": query,
            "results": ranked_results,
            "plan": "Tungsten Search -> Ferros Traversal -> Synth-Fuse Ranking"
        }

    async def orchestrate_adapters(self):
        """Manages connections to external database backends through adapters."""
        # Placeholder for adapter orchestration
        pass

    async def route_system(self, task, target_system_name):
        """Routes a specific task to one of the managed sub-systems."""
        print(f"Routing task to {target_system_name}")

        system = self.registry.get(target_system_name)
        if not system:
            raise ValueError(f"Unknown system: {target_system_name}")

        # Basic task routing logic - usually calls a primary method based on task
        if target_system_name.lower() == "neurometal":
            return await system.execute(task.get("executable"), task.get("inputs"))
        elif target_system_name.lower() == "platinum":
            return await system.parse_ast(task.get("source"))

        return {"status": "routed", "system": target_system_name}

    async def manage_ingestion(self, data_source):
        """Coordinates the ingestion pipeline across systems."""
        print(f"Managing ingestion from {data_source}")

        # 1. Logic Extraction (Platinum)
        ast = await self.platinum.parse_ast(data_source)
        ir = await self.platinum.generate_ir(ast)
        algorithms = await self.platinum.detect_algorithms(ir)

        async def process_algo(algo):
            # 2. Relationship & Lineage Tracking (Ferros)
            deps = await self.platinum.resolve_dependencies(algo)
            await self.ferros.track_lineage(algo, deps.get("dependencies", []), "dependency")

            # 3. Multi-vector Indexing (Tungsten)
            await self.tungsten.index_vectors([algo], vector_type="semantic")
            await self.tungsten.index_vectors([algo], vector_type="behavioral")

        if algorithms:
            await asyncio.gather(*(process_algo(algo) for algo in algorithms))

        return {"status": "success", "algorithms_ingested": len(algorithms)}
