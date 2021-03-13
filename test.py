import btbpython, asyncio
client = btbpython.asyncClient("API_TOKEN")

async def test():
    word = await client.word()
    madlibs = await client.madlibs()
    text = await client.text()
    lyrics = await client.lyrics("Never too late")

    lyrics2 = await client.lyrics("Never too late", "Three Days Grace")

    with open("output.txt", "w+") as f:
        f.write(f"{word}\n{madlibs}\n{text}\n{lyrics}\n\n{lyrics2}")

loop = asyncio.get_event_loop()

try:
    loop.run_until_complete(test())
finally:
    loop.close()
