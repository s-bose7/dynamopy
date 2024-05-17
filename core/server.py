from fastapi import FastAPI

from api import router
from config import config

def create_app() -> FastAPI:
    app_ = FastAPI(
        title="heisenbergDB",
        description="Fast, NoSQL, key-value-store-as-a-service",
        docs_url=None if config.ENVIRONMENT == "production" else "/docs",
        version="1.0.0",
    )
    app_.include_router(router, prefix="/heisenbergdb")
    return app_


app = create_app()

