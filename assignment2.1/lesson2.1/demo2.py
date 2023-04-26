import asyncio

async def fetch_data():
    print ("fechting data")
    await asyncio.sleep(3)
    print ("data gathered")
    return "Here the data"


async def send_data(to, data):
    print (f'Sending data {data} to {to}')
    await asyncio.sleep(2)
    print ('sending had been done...')

async def main():
    data = await fetch_data()
    print (f'data  {data}')
    await asyncio.gather(send_data('Henk', data), send_data('Karel', data))
    print ('Done')

asyncio.run(main())