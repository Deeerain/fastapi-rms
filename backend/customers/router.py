from typing import Annotated

from fastapi import APIRouter, Depends

from customers.repositories import create_repository, CustomerRepository
from customers.schemas import CustomerSchema


router = APIRouter(prefix='/customers', tags=['Customers'])


@router.get('/')
async def get_customers(repository: Annotated[CustomerRepository,
                                              Depends(create_repository)]):
    
    items = await repository.get_all()
    return items


@router.get('/{id}/')
async def get_customer(id: int,
                       repository: Annotated[CustomerRepository,
                                             Depends(create_repository)]):

    item = await repository.get(id=id)
    return item


@router.delete('/{id}/')
async def delete_customer(id: int,
                          repository: Annotated[CustomerRepository,
                                                Depends(create_repository)]):
    
    item = await repository.delete(id=id)
    return item


@router.post('/')
async def create_customer(customer: CustomerSchema,
                          repository: Annotated[CustomerRepository,
                                                Depends(create_repository)]):
    customer = await repository.create(**customer.dict())
    return customer
