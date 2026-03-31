import asyncio
import sys
import os
import unittest

# Adjust path to find atlas package
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

from atlas import (
    AtlasOrchestrator,
    PlatinumExtractor,
    NeurometalEngine,
    FerrosGraph,
    TungstenVector,
    SynthFuseEngine
)

class TestOrchestrator(unittest.TestCase):
    def setUp(self):
        self.loop = asyncio.new_event_loop()
        asyncio.set_event_loop(self.loop)

    def tearDown(self):
        self.loop.close()

    def test_orchestrator_initialization(self):
        async def run_test():
            orchestrator = AtlasOrchestrator()

            # Check that all systems are initialized
            self.assertIsInstance(orchestrator.platinum, PlatinumExtractor)
            self.assertIsInstance(orchestrator.neurometal, NeurometalEngine)
            self.assertIsInstance(orchestrator.ferros, FerrosGraph)
            self.assertIsInstance(orchestrator.tungsten, TungstenVector)
            self.assertIsInstance(orchestrator.synth_fuse, SynthFuseEngine)

            # Check that start and stop don't crash
            await orchestrator.start()
            await orchestrator.stop()

        self.loop.run_until_complete(run_test())

    def test_component_methods(self):
        async def run_test():
            orchestrator = AtlasOrchestrator()

            # Test Platinum methods
            ast = await orchestrator.platinum.parse_ast("print('hello')")
            self.assertIn("ast", ast)
            ir = await orchestrator.platinum.generate_ir(ast)
            self.assertIn("ir", ir)

            # Test Neurometal methods
            code = await orchestrator.neurometal.generate_code({"algo": "test"})
            self.assertIn("generated_code", code)

            # Test Ferros methods
            lineage = await orchestrator.ferros.track_lineage("A", "B", "dependency")
            self.assertIn("Lineage tracked", lineage)

            # Test Tungsten methods
            indexing = await orchestrator.tungsten.index_vectors([1, 2, 3])
            self.assertIn("Indexed", indexing)

            # Test Synth-Fuse methods
            fused = await orchestrator.synth_fuse.fuse_scores([])
            self.assertEqual(len(fused), 1)

        self.loop.run_until_complete(run_test())

if __name__ == '__main__':
    unittest.main()
