import btbpython, asyncio
client = btbpython.asyncClient("")
c = btbpython.client("")

async def test():
    print(await client.meme())

loop = asyncio.get_event_loop()

try:
    loop.run_until_complete(test())
finally:
    loop.close()
