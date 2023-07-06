import config

from sqlalchemy.ext.asyncio import create_async_engine, AsyncSession
from sqlalchemy.orm import declarative_base, sessionmaker

__all__ = [
    'Base',
    'get_session',
]

engine = create_async_engine(config.DB_CONNECTION_STRING)

Base = declarative_base()

async_session = sessionmaker(engine, class_=AsyncSession, expire_on_commit=False)

async def get_session() -> AsyncSession:
    '''Получение обьекта сессии'''
    async with async_session() as session:
        yield session