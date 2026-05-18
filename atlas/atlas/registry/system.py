from ..core.base import AsyncComponent

class SystemRegistry:
    """
    Registry for ATLAS sub-systems.
    Allows for decoupled registration and retrieval of specialized systems.
    """
    def __init__(self):
        self._systems = {}

    def register(self, name, system):
        if not isinstance(system, AsyncComponent):
            raise TypeError(f"System {name} must be an AsyncComponent")
        self._systems[name.lower()] = system

    def get(self, name):
        return self._systems.get(name.lower())

    def list_systems(self):
        return list(self._systems.keys())

    async def start_all(self):
        for system in self._systems.values():
            await system.start()

    async def stop_all(self):
        for system in self._systems.values():
            await system.stop()
