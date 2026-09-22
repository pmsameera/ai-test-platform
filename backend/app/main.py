from fastapi import FastAPI
from app.api.v1.health import router as health_router
from app.api.v1.requirements import router as requirements_router
from app.api.v1.testcases import router as testcases_router 
from sqlalchemy import text
from app.database import engine
from fastapi.middleware.cors import CORSMiddleware

app=FastAPI(
  title="AI Test Management Platform",
  description="Test management & execution platform",
version="0.1.0"
)

app.add_middleware(
    CORSMiddleware,
    allow_origins=["http://localhost:5173",  
                   "http://localhost:5175"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

#Base.metadata.create_all(bind=engine)

app.include_router(
    health_router
)

app.include_router(
    requirements_router
)

app.include_router(
    testcases_router
)

@app.get('/')
def root():
    return {
        "message" : "Welcome to the AI Test Management Platform"
    }

@app.get("/api/v1/db-check")
def db_check():
    with engine.connect() as connection:
        result = connection.execute(text("SELECT 1"))
        
    return {
        "database": "connected"
    }
