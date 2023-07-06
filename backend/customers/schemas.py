from datetime import datetime

from pydantic import BaseModel


__all__ = [
    'CustomerSchema',
    'CustomerModel',
]


class CustomerSchema(BaseModel):
    first_name: str
    last_name: str
    tel: str

    class Config:
        orm_mode = True


class CustomerModel(CustomerSchema):
    id: int
    created_at: datetime
    updated_at: datetime
