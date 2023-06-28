import aiohttp
import asyncio

class NetworkClient:
    def __init__(self, base_url):
        self.base_url = base_url

    async def to_fetch(self):
        async with aiohttp.ClientSession() as session:
            async with session.get(f'{self.base_url}') as resp:
                print(resp.status)
                print(await resp.text())

async def main():
    tasks = [
        NetworkClient("http://localhost:9000/data/all").to_fetch(),
        NetworkClient("http://localhost:9000/data/1997").to_fetch(),
        NetworkClient("http://localhost:9000/data/1997/2002").to_fetch()
    ]
    await asyncio.gather(*tasks)
if __name__ == '__main__':
    asyncio.run(main())