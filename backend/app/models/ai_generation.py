from sqlalchemy import Column, Integer, String, ForeignKey, Text, DateTime
from sqlalchemy.sql import func
from sqlalchemy.orm import relationship
from sqlalchemy.dialects.postgresql import JSONB

from app.database import Base

class AIGeneration(Base):
    __tablename__ = "ai_generations"

    id = Column(Integer, primary_key=True, index=True)

    requirement_id = Column(
        Integer,
        ForeignKey("requirements.id"),
        nullable=False,
    )

    model = Column(String(100), nullable=False)

    prompt = Column(Text, nullable=False)

    response = Column(JSONB, nullable=False)

    status = Column(
        String(50),
        nullable=False,
        default="PENDING_REVIEW",
    )

    created_at = Column(
        DateTime(timezone=True),
        server_default=func.now(),
    )
