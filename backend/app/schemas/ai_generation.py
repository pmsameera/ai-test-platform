from datetime import datetime

from pydantic import BaseModel


class AIGenerationCreate(BaseModel):
    requirement_id: int

class AIGenerationResponse(BaseModel):
    id: int
    requirement_id: int
    model: str
    prompt: str
    response: str
    status: str
    created_at: datetime

    model_config = {
        "from_attributes": True
    }   