import asyncio

from app.database import Base, async_engine
from app.models import concerts, places, tickets, users  # noqa: F401


async def main():
    async with async_engine.begin() as conn:
        await conn.run_sync(Base.metadata.create_all)


if __name__ == "__main__":
    asyncio.run(main())
