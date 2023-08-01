from abc import ABC, abstractmethod

from typing import TypeVar, Type, Optional, Any, Iterable, List
from sqlalchemy import Select, delete, insert, select, update
from sqlalchemy.exc import SQLAlchemyError
from pydantic import BaseModel
from sqlalchemy.orm import selectinload

from db.db import async_session_maker

Model = TypeVar("Model", bound="Base")
BM = TypeVar("BM", bound=BaseModel)


class AbstractRepository(ABC):
    @abstractmethod
    async def add_one():
        raise NotImplementedError

    @abstractmethod
    async def get_list():
        raise NotImplementedError

    @abstractmethod
    async def delete():
        raise NotImplementedError

    @abstractmethod
    async def update():
        raise NotImplementedError


class SQLAlchemyRepository(AbstractRepository):
    model = None
    TKwargs = Optional[Any]

    async def add_one(self, data: dict) -> int:
        async with async_session_maker() as session:
            stmt = insert(self.model).values(**data).returning(self.model.id)
            res = await session.execute(stmt)
            await session.commit()
            return res.scalar_one()

    async def get_item_by_id(self, item_id: int, **kwargs: TKwargs) -> Optional[Model]:
        async with async_session_maker() as session:
            query = self._construct_query(select(self.model), **kwargs)
            try:
                q = await session.execute(query.where(self.model.id == item_id))
            except SQLAlchemyError as exc:
                print(exc.args)
                raise
            else:
                item: Optional[Model] = q.scalar_one_or_none()
            return item

    async def get_list(self, **kwargs: TKwargs) -> list[Model] | Any:
        async with async_session_maker() as session:
            query = self._construct_query(select(self.model), **kwargs)
            q = await session.execute(query)
            results = q.scalars().all()
            return results

    async def delete(self, item_id: int) -> bool:
        async with async_session_maker() as session:
            item = await self.get_item_by_id(item_id)
            if not item:
                return False
            try:
                await self.session.execute(
                    delete(self.model).where(self.model.id == item_id)
                )
                await self.session.flush()
            except SQLAlchemyError as exc:
                print(exc.args)
                raise
            return True

    async def update(
        self, item_id: int, item: BM, exclude_none: bool = True, **kwargs: TKwargs
    ) -> Optional[Model]:
        async with async_session_maker() as session:
            try:
                await self.session.execute(
                    update(self.model)
                    .where(self.model.id == item_id)
                    .values(**item.dict(exclude_none=exclude_none))
                )
                await self.session.flush()
            except SQLAlchemyError as exc:
                print(exc.args)
                raise
            return await self.get_item_by_id(item_id, **kwargs)

    def _construct_query(
        self,
        query: Select,
        where: Optional[Iterable] = None,
        select_in_load: Optional[Iterable] = None,
        order_by: Optional[Iterable] = None,
        limit: Optional[int] = None,
        offset: Optional[int] = None,
    ) -> Select:
        if where:
            query = query.where(*where)
        if select_in_load:
            for option in select_in_load:
                query = query.options(selectinload(option))
        if order_by:
            query = query.order_by(*order_by)
        if limit is not None:
            query = query.limit(limit)
        if offset is not None:
            query = query.offset(offset)

        return query
