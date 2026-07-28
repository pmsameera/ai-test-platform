from pydantic import BaseModel

class RequirementCreate(BaseModel):
    title: str
    description: str

class RequirementResponse(BaseModel):
    id: int
    title: str
    description: str

    model_config = {
        "from_attributes": True
    }

class RequirementUpdate(BaseModel):
    title: str | None = None
    description: str | None = None