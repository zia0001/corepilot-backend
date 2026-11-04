from fastapi import FastAPI
from pydantic import BaseModel






app = FastAPI()


@app.get("/health")
async def check_health():
    return {"status": "ok"}



