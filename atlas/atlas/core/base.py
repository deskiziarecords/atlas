# atlas/core/base.py
class AsyncComponent:
    """Base class for all asynchronous components in the ATLAS system."""
    async def start(self):
        """Initializes the component."""
        pass

    async def stop(self):
        """Shuts down the component."""
        pass
