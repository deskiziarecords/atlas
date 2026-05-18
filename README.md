# ATLAS: Universal Database Orchestrator

ATLAS is "The Father" system that coordinates five specialized systems: **Platinum**, **Neurometal**, **Ferros**, **Tungsten**, and **Synth-Fuse**.

## Architecture: Standalone vs. Embedded
ATLAS is designed as a **Standalone Orchestrator**.

### Why Standalone?
1. **Centralized Intelligence**: ATLAS owns the high-level query planning and routing logic. Sub-systems like Ferros or Tungsten don't need to know about each other; they only need to respond to ATLAS.
2. **Decoupling**: Specialized systems (like Neurometal) can be swapped or scaled independently without affecting the other systems.
3. **The "Father" Role**: As the orchestrator, ATLAS manages the lifecycle (`start`/`stop`) of all sub-systems through a central `SystemRegistry`.

### Data Flow
- **Ingestion**: `Code -> PLATLAS (Platinum) -> ATLAS (Orchestrator) -> [Ferros, Tungsten]`.
- **Querying**: `User Query -> ATLAS -> [Tungsten Search, Ferros Traversal] -> Synth-Fuse -> User`.

## Core Systems
- **Platinum**: Logic Extraction (AST, IR, Algorithm Detection)
- **Neurometal**: Execution & Translation (Code Generation, Optimization, Runtime)
- **Ferros**: Graph System (Relationships, Lineage, Dependency Graphs)
- **Tungsten**: Vector System (Multi-vector indexing, Similarity search)
- **Synth-Fuse**: Fusion Engine (Score fusion, Ranking, Aggregation)

## Usage

### 1. Initialization
The `AtlasOrchestrator` is the primary entry point.

```python
import asyncio
from atlas import AtlasOrchestrator

async def main():
    orchestrator = AtlasOrchestrator()
    await orchestrator.start()

    # ... use orchestrator ...

    await orchestrator.stop()

if __name__ == "__main__":
    asyncio.run(main())
```

### 2. Ingesting Data
The ingestion pipeline extracts logic, tracks relationships, and indexes vectors.

```python
source_code = "def my_algorithm(): pass"
ingestion_result = await orchestrator.manage_ingestion(source_code)
print(f"Ingested {ingestion_result['algorithms_ingested']} algorithms.")
```

### 3. Planning and Executing Queries
The query planner coordinates Tungsten, Ferros, and Synth-Fuse to find and rank relevant results.

```python
query = "Search for algorithms related to graph traversal"
plan = await orchestrator.plan_query(query)

for result in plan['results']:
    print(f"Found: {result}")
```

### 4. Routing Tasks
Directly route tasks to specific sub-systems like Neurometal for execution.

```python
task = {
    "executable": "generated_code_block",
    "inputs": {"data": [1, 2, 3]}
}
result = await orchestrator.route_system(task, "neurometal")
print(f"Execution result: {result}")
```

### 5. Specialized System Access
If you need direct access to a sub-system while still going through the orchestrator:

```python
ferros = orchestrator.registry.get("ferros")
graph_info = await ferros.build_dependency_graph("root_node")
```

## Running Tests
To run the test suite:
```bash
python3 -m unittest discover atlas/tests
```
