import btbpython, asyncio
client = btbpython.asyncClient("")

async def test():
    word = await client.word()
    print(word)

loop = asyncio.get_event_loop()

try:
    loop.run_until_complete(test())
finally:
    loop.close()
