from fastapi import APIRouter

from backend.apis.general_route import login

api_router = APIRouter()
api_router.include_router(login.router, prefix="/login", tags=["login"])