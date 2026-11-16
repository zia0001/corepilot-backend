from fastapi import FastAPI
from app.api.health import router as health_router






app = FastAPI()

#Method that connects an APIRouter's endpoints to the main FastAPI app
app.include_router(health_router)
