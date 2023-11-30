import asyncio
async def example_coroutine():
    print("start coroutine")
    await asyncio.sleep(1)
    print('end coroutine')

#Run coroutine
asyncio.run(example_coroutine())


