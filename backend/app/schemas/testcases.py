from pydantic import BaseModel, Field

class TestCaseBase(BaseModel):
    title:str = Field(..., min_length=1)
    description:str = Field(..., min_length=1)
    steps:str = Field(..., min_length=1)
    expected_result:str = Field(..., min_length=1)

class TestCaseCreate(TestCaseBase):
    requirement_id:int

class TestCaseResponse(TestCaseBase):
    id: int
    requirement_id:int
    actual_result:str

    model_config = {
        "from_attributes": True
    }

class TestCaseUpdate(BaseModel):
    title: str | None = Field(None, min_length=1)
    description: str | None = Field(None, min_length=1)
    steps: str | None = Field(None, min_length=1)
    expected_result: str | None = Field(None, min_length=1)
    actual_result: str | None = Field(None, min_length=1)