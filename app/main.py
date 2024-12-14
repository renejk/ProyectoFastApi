from fastapi import APIRouter, FastAPI
from app.routers import user_router, event_router


app = FastAPI()

api_v1 = APIRouter(prefix="/api/v1")
api_v1.include_router(user_router)
api_v1.include_router(event_router)
app.include_router(api_v1)

