import asyncio

def mul(x, y):
    return x * y

async def mul(x, y):
    return x * y

loop = asyncio.get_event_loop()

try:
    res2 = loop.run_until_complete(mul(5, 5))
    print(res2)

finally:
    loop.close()