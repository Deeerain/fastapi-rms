from typing import Any

from sqlalchemy import select
from sqlalchemy.ext.asyncio import AsyncSession


__all__ = [
    'BaseRepository',
    'SqlalchemyRepository',
]


class BaseRepository:
    def get_all(self, *args, **kwargs) -> Any:
        raise NotImplementedError
    
    def get(self, *args, **kwargs) -> Any:
        raise NotImplementedError
    
    def create(self, *args, **kwargs) -> Any:
        raise NotImplementedError
    
    def update(self, *args, **kwargs) -> Any:
        raise NotImplementedError
    
    def delete(self, *args, **kwargs) -> Any:
        raise NotImplementedError


class SqlalchemyRepository(BaseRepository):
    def __init__(self, model, session: AsyncSession) -> None:
        self._session = session
        self._model = model

    async def _filtered_query(self, **kwargs):
        return await self._session.execute(select(self._model).filter_by(**kwargs))

    async def get_all(self, **kwargs) -> Any:
        items = await self._filtered_query(**kwargs)
        await self._session.close()
        return items.scalars().all()
    
    async def get(self, **kwargs) -> Any:
        items = await self._filtered_query(**kwargs)
        await self._session.close()
        return items.scalar_one_or_none()

    async def create(self, **kwargs) -> Any:
        instance = self._model(**kwargs)
        self._session.add(instance)
        await self._session.commit()
        await self._session.refresh(instance)
        await self._session.close()
        return instance

    async def delete(self, **kwargs) -> Any:
        items = await self._filtered_query(**kwargs)
        item = items.scalar_one_or_none()
        if item:
            await self._session.delete(item)
            await self._session.commit()

        await self._session.close()
        return item