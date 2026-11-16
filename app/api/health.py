from fastapi import APIRouter

router = APIRouter()  # Organizes related API routes into a separate module


@router.get("/health")
async def check_health():
    return {"status": "ok"} 
