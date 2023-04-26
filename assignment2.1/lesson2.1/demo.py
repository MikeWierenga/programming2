import asyncio
import time

def count():
    print ('one')
    time.sleep(1)
    print ('two')

async def count1():
    print("one")
    await asyncio.sleep(3)
    print ("two")


async def main():
    tasks = [ count1(),count1(), count1() ]
    await asyncio.gather(*tasks)


if __name__ == '__main__':
    asyncio.run(main())
