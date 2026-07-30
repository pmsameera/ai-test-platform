from fastapi import APIRouter

router=APIRouter(prefix="/api/v1/health", tags=["Health"])

@router.get('/health')
def health_check():
    return {
        "status":"healthy",
        "service": "ai-test-platform-api",
        "version": "0.1.0"
    }