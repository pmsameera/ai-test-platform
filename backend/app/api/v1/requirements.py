from fastapi import APIRouter
from app.database import get_db
from sqlalchemy.orm import Session
from fastapi import Depends
from app.schemas.requirement import RequirementCreate, RequirementResponse, RequirementUpdate
from app.models.requirement import Requirement
from fastapi import HTTPException

router=APIRouter(
    prefix="/api/v1/requirements",
    tags=["Requirements"]
)

@router.post('/', response_model=RequirementResponse)
def create_requirement(
    requirement: RequirementCreate,
    db: Session = Depends(get_db)
):
    new_requirement = Requirement(
        title=requirement.title,
        description=requirement.description
    )

    db.add(new_requirement)
    db.commit()
    db.refresh(new_requirement)

    return new_requirement

@router.get('/', response_model=list[RequirementResponse])
def get_requirements(db: Session = Depends(get_db)):
    requirements = db.query(Requirement).all()
    return requirements

@router.get('/{requirement_id}', response_model=RequirementResponse)
def get_requirement(requirement_id: int, db: Session = Depends(get_db)):
    requirement = db.query(Requirement).filter(Requirement.id == requirement_id).first()
    if not requirement:
        raise HTTPException(status_code=404, detail =" Requirement not found")
    return requirement

@router.patch('/{requirement_id}', response_model=RequirementResponse)
def update_requirement(
    requirement_id: int,
    requirement_update: RequirementUpdate,
    db: Session = Depends(get_db)
):
    requirement = db.query(Requirement).filter(Requirement.id == requirement_id).first()
    if not requirement:
        raise HTTPException(status_code=404, detail="Requirement not found")

    if requirement_update.title is not None:
        requirement.title = requirement_update.title
    if requirement_update.description is not None:
        requirement.description = requirement_update.description

    db.commit()
    db.refresh(requirement)

    return requirement

@router.delete('/{requirement_id}')
def delete_requirement(requirement_id: int, db: Session = Depends(get_db)):
    requirement = db.query(Requirement).filter(Requirement.id ==requirement_id).first()
    if not requirement:
        raise HTTPException(status_code=404, detail="Requirement not found")

    db.delete(requirement)
    db.commit() 

    return {"message": "Requirement deleted successfully"}