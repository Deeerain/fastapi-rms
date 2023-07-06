import config

from sqlalchemy.ext.asyncio import create_async_engine, AsyncSession
from sqlalchemy.orm import declarative_base, sessionmaker


__all__ = [
    'Base',
    'get_session',
]


engine = create_async_engine(config.DB_CONNECTION_STRING)

Base = declarative_base()
Base.metadata.bind = engine
async_session = sessionmaker(engine, class_=AsyncSession, expire_on_commit=False)
