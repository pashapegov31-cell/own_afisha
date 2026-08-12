from contextlib import asynccontextmanager

from fastapi import FastAPI
from redis.asyncio import ConnectionPool, Redis


@asynccontextmanager
async def lifespan(app: FastAPI):
    app.state.redis_pool = ConnectionPool(
        host="localhost",
        db=0,
        port=6379,
        protocol=2,
        decode_reaponses=True,
        max_connections=10,
    )

    app.state.redis = Redis(connection_pool=app.state.redis_pool)

    yield

    await app.state.redis.close()
    await app.state.redis_pool.disconnect()


app = FastAPI(lifespan=lifespan)
