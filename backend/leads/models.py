from db import Base

from sqlalchemy import Column, Integer, String, DateTime
from sqlalchemy.sql import func


__all__ = [
    'Lead',
]


class Lead(Base):
    __tablename__ = 'leads'

    id = Column(Integer, primary_key=True, autoincrement=True, index=True)
    first_name = Column(String, index=True)
    last_name = Column(String, index=True, nullable=True)
    tel = Column(String, index=True, nullable=False)
    created_at = Column(DateTime(timezone=True), server_default=func.now(), index=True)
