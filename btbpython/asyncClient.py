import asyncio, aiohttp, json

class asyncClient:
    def __init__(self, token:str):
        self.settings = {"headers":{"Authorization": token}}
        self.BASE = "https://api.bytestobits.dev"

    async def create_request(self, endpoint, **kwargs):
        url = self.BASE + endpoint +"?" + '&'.join(f"{i}={kwargs[i]}" for i in kwargs)

        async with aiohttp.ClientSession() as session:
            async with session.get(url, **self.settings) as request:
                return await request.text()

    async def word(self):
        _data = json.loads(await self.create_request("/word"))
        return _data

    async def madlibs(self):
        _data = json.loads(await self.create_request("/madlibs"))
        return _data

    async def text(self):
        _data = await self.create_request("/text")
        return _data

    async def meme(self):
        _data = json.loads(await self.create_request("/meme"))
        return _data

    async def lyrics(self, song, artist=None):
        _params = {
            "song": song
        }
        if artist:
            _params["artist"] = artist
        _data = json.loads(await self.create_request("/lyrics", **_params))
        return _data

    async def reddit(self, subreddit, limit=None):
        _params = {
            "subreddit": subreddit
        }
        if limit:
            _params["limit"] = limit
        _data = json.loads(await self.create_request("/reddit", **_params))
        return _data

    async def info(self):
        _data = await self.create_request("/info")
        return _data
