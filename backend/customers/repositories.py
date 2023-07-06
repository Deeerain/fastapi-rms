from typing import Any

from db import async_session

from utils.repositories import SqlalchemyRepository

from customers.models import Customer


__all__ = [
    'CustomerRepository',
]


class CustomerRepository(SqlalchemyRepository):
    pass


def create_repository():
    return CustomerRepository(Customer, async_session())