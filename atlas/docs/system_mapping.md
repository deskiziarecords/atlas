# Final Role Mapping (Authoritative)

## 1. Platinum
**Role:** Logic Extraction System
**Owns:** AST parsing, IR generation, algorithm detection, dependency closure
**Outputs:** Algorithm Objects -> ATLAS

## 2. Neurometal
**Role:** Execution / Translation Engine
**Owns:** code generation, JAX / Rust / etc translation, optimization, runtime execution

## 3. Ferros
**Role:** Graph System
**Owns:** algorithm relationships, lineage tracking, dependency graphs, traversal logic
**Backends:** Neo4j, NetworkX

## 4. Tungsten
**Role:** Vector System
**Owns:** multi-vector indexing + similarity search (semantic, structural, behavioral vectors)
**Backends:** FAISS, HNSW, Chroma

## 5. Synth-Fuse
**Role:** Fusion Engine
**Owns:** score fusion, ranking, multi-vector weighting, cross-system aggregation

## 6. ATLAS
**Role:** Universal Database Orchestrator (THE "FATHER")
**Owns:** query planning, adapter orchestration, system routing, ingestion pipeline
