import logging
import asyncio
import aioredis
from aiohttp import web

REDIS_URL = 'redis://redis'

loop = asyncio.get_event_loop()


async def add(request):
    connection = await aioredis.create_connection(
        REDIS_URL, loop=loop)
    await connection.execute('set', '123', 'hehehe')
    connection.close()
    await connection.wait_closed()
    return web.Response(text="done")


async def retrieve(request: web.Request):
    key = request.match_info['key']
    connection = await aioredis.create_connection(
        REDIS_URL, loop=loop)
    value = await connection.execute('get', key)
    connection.close()
    await connection.wait_closed()
    return web.Response(text=value.decode('utf-8'))

shortener = web.Application(loop=loop)
shortener.add_routes([
    web.get('/add', add),
    web.get('/{key:\d+}', retrieve),
])
web.run_app(shortener)
