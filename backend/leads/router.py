from typing import Annotated

from fastapi import APIRouter, Depends
from fastapi import Response

from leads.repositories import LeadRepository, create_repository
from leads.schemas import CreateLeadSchema, LeadSchema


router = APIRouter(prefix='/leads', tags=['Leads'])


@router.get('/')
async def get_leads(repository: Annotated[LeadRepository, Depends(create_repository)]):
    leads = await repository.get_all()
    return [LeadSchema.from_orm(lead) for lead in leads]


@router.post('/')
async def crete_lead(lead: CreateLeadSchema,
                     repository: Annotated[LeadRepository, Depends(create_repository)]):
    new_lead = await repository.create(**lead.dict())
    return LeadSchema.from_orm(new_lead)


@router.get('/{id}/')
async def get_lead(id: int,
                   repository: Annotated[LeadRepository, Depends(create_repository)]):
    lead = await repository.get(id=id)
    
    if lead is None:
        return Response(status_code=404)
    
    return LeadSchema.from_orm(lead)


@router.delete('/{id}/')
async def delete_lead(id: int, 
                      repository: Annotated[LeadRepository, Depends(create_repository)]):
    lead = await repository.delete(id=id)
    return lead