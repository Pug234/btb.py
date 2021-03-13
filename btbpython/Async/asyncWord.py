from .asyncRequest import request
import asyncio

async def word(token):
    return await request("https://api.bytestobits.dev/word", token)
