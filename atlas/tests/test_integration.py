import asyncio
import sys
import os
import unittest

# Adjust path to find atlas package
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

from atlas import AtlasOrchestrator

class TestIntegration(unittest.TestCase):
    def setUp(self):
        self.loop = asyncio.new_event_loop()
        asyncio.set_event_loop(self.loop)
        self.orchestrator = AtlasOrchestrator()

    def tearDown(self):
        self.loop.close()

    def test_full_workflow(self):
        async def run_test():
            await self.orchestrator.start()

            # 1. Test Ingestion
            source_code = "def sample_algo(): pass"
            ingestion_result = await self.orchestrator.manage_ingestion(source_code)
            self.assertEqual(ingestion_result["status"], "success")
            self.assertGreater(ingestion_result["algorithms_ingested"], 0)

            # 2. Test Query Planning
            query = "Find algorithms similar to sample_algo"
            query_result = await self.orchestrator.plan_query(query)
            self.assertEqual(query_result["query"], query)
            self.assertIn("results", query_result)
            self.assertIn("Tungsten Search -> Ferros Traversal -> Synth-Fuse Ranking", query_result["plan"])

            # 3. Test Routing (e.g., to Neurometal for execution)
            task = {
                "executable": "generated_code_block",
                "inputs": {"x": 10}
            }
            routing_result = await self.orchestrator.route_system(task, "neurometal")
            self.assertEqual(routing_result["result"], "success")

            await self.orchestrator.stop()

        self.loop.run_until_complete(run_test())

if __name__ == '__main__':
    unittest.main()
