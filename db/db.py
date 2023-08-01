from typing import Any, AsyncGenerator

from sqlalchemy import MetaData
from sqlalchemy.ext.asyncio import AsyncSession, async_sessionmaker, create_async_engine
from sqlalchemy.orm import as_declarative, declared_attr

import inflection
from utils.config import settings

engine = create_async_engine(settings.get_db_uri)
async_session_maker = async_sessionmaker(engine, expire_on_commit=False)

metadata = MetaData()


@as_declarative()
class Base:
    id: Any
    __name__: str

    @declared_attr  # type: ignore
    def __tablename__(self) -> str:
        return inflection.underscore(self.__name__)


# async def get_db() -> AsyncGenerator:
#     db = AsyncSession(bind=create_async_engine(settings.get_db_uri, future=True, echo=False), autocommit=False,
#                       autoflush=False, expire_on_commit=False)
#     try:
#         yield db
#     finally:
#         await db.close()


async def get_async_session():
    async with async_session_maker() as session:
        yield session
