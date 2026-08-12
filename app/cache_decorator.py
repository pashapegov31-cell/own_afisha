import json
from functools import wraps

from fastapi import HTTPException, Request
from redis.asyncio import Redis


def cache(ttl: int = 60):
    """Декоратор хэширования GET-запросов для меня(мб доделается для тебя тоже)"""

    def decorator(func):
        @wraps(func)
        async def wrapper(request: Request, *args, **kwargs):
            redis: Redis = request.app.state.redis
            cache_key = f"{request.url.path}:{request.query_params}"
            cache = await redis.get(cache_key)
            if cache:
                return json.loads(cache)
            result = await func(request, *args, **kwargs)
            if not result:
                raise HTTPException(status_code=401, detail="Nothing found")

            try:
                await redis.set(cache_key, json.dumps(result), ex=ttl)
            except TypeError:
                pass

            return result

        return wrapper

    return decorator
