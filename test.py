import asyncio

# loop = asyncio.ProactorEventLoop()
# asyncio.set_event_loop(loop)

async def example_async_function():
    print("Start")
    await asyncio.sleep(2)  # Simulate an asynchronous task (e.g., I/O operation)
    print("End")

# Run the asynchronous function in an event loop
asyncio.run(example_async_function())
