from pydantic import BaseModel, Field

class RequirementCreate(BaseModel):
    title: str = Field(..., min_length=1)
    description: str = Field(..., min_length=1)

class RequirementResponse(BaseModel):
    id: int
    title: str = Field(..., min_length=1)
    description: str = Field(..., min_length=1)

    model_config = {
        "from_attributes": True
    }

class RequirementUpdate(BaseModel):
    title: str | None = Field(None, min_length=1)
    description: str | None = Field(None, min_length=1)