from fastapi import APIRouter

from api.v1.get import get_router
from api.v1.store import store_router
from api.v1.delete import delete_router

v1_router = APIRouter()
v1_router.include_router(router=store_router, prefix="/store")
v1_router.include_router(router=get_router, prefix="/get")
v1_router.include_router(router=delete_router, prefix="/delete")