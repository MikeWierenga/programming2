import asyncio
from aiohttp import ClientSession
import math,random

async def get_data(url, fn):
    print (f'fetching data from {url}')
    async with ClientSession() as session:
        resp = await session.request(method='GET', url=url)
        json = await resp.json()
    fn(json)


def print_data(data):
    print (data)

async def kill_time(nr):
    await asyncio.sleep(math.floor(random.random() * 10))
    print (f'demo-delay {nr}')


async def main():
    tasks = [ kill_time(1),
        get_data('http://jsonplaceholder.typicode.com/todos/1', print_data),
        kill_time(2),
        kill_time(3) ]
    await asyncio.gather(*tasks)

    print ('done')

asyncio.run(main())