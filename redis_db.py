import asyncio

import redis.asyncio as aioredis


async def main():
    redis_client = aioredis.Redis(
        host="localhost",
        port=6379,
        db=0,
        protocol=2,
        decode_responses=True,
    )
    async with redis_client as r:
        pass


if __name__ == "__main__":
    asyncio.run(main())
