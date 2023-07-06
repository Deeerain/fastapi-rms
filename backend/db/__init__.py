from sqlalchemy.ext.asyncio import create_async_engine, AsyncSession
from sqlalchemy.orm import declarative_base, sessionmaker

engine = create_async_engine('postgresql+asyncpg://scott:tiger@localhost/test')

Base = declarative_base()

async_session = sessionmaker(engine, class_=AsyncSession, expire_on_commit=False)