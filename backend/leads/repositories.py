from db import async_session

from utils.repositories import SqlalchemyRepository

from leads.models import Lead


__all__ = [
    'LeadRepository',
    'create_repository',
]


class LeadRepository(SqlalchemyRepository):
    pass


def create_repository():
    return LeadRepository(Lead, async_session())