from fastapi import APIRouter

router=APIRouter()

@router.get('/health')
def health_check():
    return {
        "status":"healthy",
        "service": "ai-test-platform-api",
        "version": "0.1.0"
    }