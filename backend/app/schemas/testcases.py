from pydantic import BaseModel

class TestCaseBase(BaseModel):
    title:str
    description:str
    steps:str
    expected_result:str 

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
    title: str | None = None
    description: str | None = None
    steps: str | None = None
    expected_result: str | None = None
    actual_result: str | None = None