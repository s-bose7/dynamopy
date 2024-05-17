from fastapi import APIRouter

from get import get_router
from store import store_router

v1_router = APIRouter()
v1_router.include_router(router=get_router, prefix="/get")
v1_router.include_router(router=store_router, prefix="/store")