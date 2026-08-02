from fastapi import APIRouter
from app.models.testcase import TestCase
from app.schemas.testcases import TestCaseCreate, TestCaseResponse, TestCaseUpdate 
from app.database import get_db
from sqlalchemy.orm import Session
from fastapi import Depends, HTTPException 

router = APIRouter(
    prefix="/api/v1/testcases",
    tags=["Test Cases"])


@router.get('/', response_model=list[TestCaseResponse])
def get_testcases(db : Session = Depends(get_db)):
    testcases = db.query(TestCase).all()
    return testcases


@router.get('/{testcase_id}', response_model=TestCaseResponse)
def get_testcase(testcase_id: int, db: Session = Depends(get_db)):
    testcase = db.query(TestCase).filter(TestCase.id == testcase_id).first()
    if not testcase:
        raise HTTPException(status_code=404, detail="Testcase not found")
    return testcase


@router.get('/requirement/{requirement_id}', response_model=list[TestCaseResponse])
def get_testcase_by_requirement(requirement_id: int, db: Session = Depends(get_db)):
    testcases = db.query(TestCase).filter(TestCase.requirement_id == requirement_id).all()
    if not testcases:
        raise HTTPException(status_code=404, detail="Testcases not found")
    return testcases


@router.post('/', response_model=TestCaseResponse)
def create_testcase(testcase : TestCaseCreate, db : Session = Depends(get_db)):
    new_testcase = TestCase(
        requirement_id=testcase.requirement_id,
        title=testcase.title,
        description=testcase.description,
        steps=testcase.steps,
        expected_result=testcase.expected_result
    )
    db.add(new_testcase)
    db.commit()
    db.refresh(new_testcase)
    return new_testcase
   

@router.patch('/{testcase_id}', response_model = TestCaseResponse)
def update_testcase(testcase_id: int, testcase: TestCaseUpdate, db: Session = Depends(get_db)):
    updated_testcase = db.query(TestCase).filter(TestCase.id == testcase_id).first()
    if not updated_testcase:
        raise HTTPException(status_code=404, detail="Testcase not found")
    if testcase.title is not None:
        updated_testcase.title = testcase.title
    if testcase.description is not None:
        updated_testcase.description = testcase.description
    if testcase.steps is not None:
        updated_testcase.steps = testcase.steps
    if testcase.expected_result is not None:
        updated_testcase.expected_result = testcase.expected_result
    if testcase.actual_result is not None:
        updated_testcase.actual_result = testcase.actual_result
    db.commit()
    db.refresh(updated_testcase)
    return updated_testcase

        
@router.delete('/{testcase_id}')
def delete_testcase(testcase_id: int, db: Session = Depends(get_db)):
    delete_testcase = db.query(TestCase).filter(TestCase.id == testcase_id).first()
    if not delete_testcase:
        raise HTTPException(status_code=404, detail="Testcase not found")
    db.delete(delete_testcase)
    db.commit() 
    return {"message": f"Deleted test case with ID {testcase_id}"}