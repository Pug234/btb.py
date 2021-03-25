import btbpython, asyncio
client = btbpython.asyncClient("Gww3.XPWIDQAdahXyNXsGn0Xw")
c = btbpython.client("Gww3.XPWIDQAdahXyNXsGn0Xw")

async def test():
    song = await client.Lyrics('my play')
    print(await song.raw())
loop = asyncio.get_event_loop()

try:
    loop.run_until_complete(test())
finally:
    loop.close()
