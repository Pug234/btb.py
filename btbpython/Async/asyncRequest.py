import aiohttp, asyncio, requests, json

async def request(url, token):

    async with aiohttp.ClientSession() as session:
            async with session.get(url, headers=token) as request:
                r = request

    if r.status == 429:
      raise Exception(f'API response: {r.status_code}: To many request')

    return await r.json()
