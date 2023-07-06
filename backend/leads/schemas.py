from pydantic import BaseModel


class LeadSchemaBase(BaseModel):
    first_name: str
    last_name: str
    tel: str

    class Config:
        orm_mode = True


class LeadSchema(LeadSchemaBase):
    id: int


class CreateLeadSchema(LeadSchemaBase):
    pass
