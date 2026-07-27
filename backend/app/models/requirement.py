from sqlalchemy import Column, Integer, String

from app.database import Base


class Requirement(Base):
    __tablename__ = "requirements"

    id = Column(Integer, primary_key=True, index=True)
    title = Column(String, nullable=False)
    description = Column(String, nullable=False)