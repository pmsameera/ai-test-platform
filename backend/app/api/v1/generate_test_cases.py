from app.services.ai_service import AIService
from app.database import get_db
from app.models.requirement import Requirement
from app.models.ai_generation import AIGeneration
from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session

router=APIRouter(prefix="/api/v1/requirements", tags=["Requirements"])

@router.post("/{requirement_id}/generate-test-cases")
def generate_test_cases(requirement_id: int, db: Session = Depends(get_db)):
    requirement = (
        db.query(Requirement)
        .filter(Requirement.id == requirement_id)
        .first()
    )

    if not requirement:
        raise HTTPException(
            status_code=404,
            detail="Requirement not found",
        )

    ai_service = AIService()
    ai_result = ai_service.generate_test_cases(requirement.title, requirement.description)
    generation = AIGeneration(
    requirement_id=requirement.id,
    model=ai_result["model"],
    prompt=ai_result["prompt"],
    response=ai_result["response"],
    status="PENDING_REVIEW",
    )

    db.add(generation)
    db.commit()
    db.refresh(generation)
    