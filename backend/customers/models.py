from sqlalchemy import (
    Column, String, Integer, DateTime, func)

from db import Base


__all__ = [
    'Customer'
]


class Customer(Base):
    __tablename__ = 'customers'

    id = Column(Integer, autoincrement=True, index=True, primary_key=True)
    first_name = Column(String, index=True)
    last_name = Column(String, index=True, nullable=True)
    tel = Column(String, index=True)
    creted_at = Column(DateTime(timezone=True), server_default=func.now())
    updated_at = Column(DateTime(timezone=True), server_onupdate=func.now())