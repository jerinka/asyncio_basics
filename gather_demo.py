import asyncio

async def fetch_data(url):
    # Your asynchronous code to fetch data from the URL
    asyncio.sleep(1)
    print('url:',url)

async def main():
    urls = ['url1', 'url2', 'url3']
    tasks = [fetch_data(url) for url in urls]
    await asyncio.gather(*tasks)

asyncio.run(main())