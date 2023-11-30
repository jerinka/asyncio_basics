import asyncio

async def example_coroutine():
    try:
        # Your async code here
        shsh()
    except Exception as e:
        print(f'An error occured: {e}')

asyncio.run(example_coroutine())