from fastapi import FastAPI
from app.api.v1.health import router as health_router

app=FastAPI(
  title="AI Test Management Platform",
  description="Test management & execution platform",
version="0.1.0"
)

app.include_router(
    health_router,
    prefix="/api/v1"
)

@app.get('/')
def root():
    return {
        "message" : "Welcome to the AI Test Management Platform"
    }