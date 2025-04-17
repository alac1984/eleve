import os

from sqlmodel import SQLModel, create_engine
from sqlmodel.ext.asyncio.session import AsyncSession
from sqlalchemy.ext.asyncio import AsyncEngine
from dotenv import load_dotenv
from sqlalchemy.orm import sessionmaker

from eleve.repository import *

load_dotenv()

DATABASE_URL = os.environ.get("DATABASE_URL")

engine = AsyncEngine(create_engine(DATABASE_URL, echo=True, future=True))  # type: ignore

async def init_db():
    async with engine.begin() as conn:
        # await conn.run_sync(SQLModel.metadata.drop_all)
        await conn.run_sync(SQLModel.metadata.create_all)


async def get_session() -> AsyncSession:  # type: ignore
    async_session = sessionmaker(
        engine, class_=AsyncSession, expire_on_commit=False
    )
    async with async_session() as session:
        yield session


if __name__ == "__main__":
    breakpoint()
    print(dir(engine))
