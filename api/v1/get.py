from typing import Any

from fastapi import APIRouter, Request

from datetime import datetime
from pydantic import BaseModel, Field, ValidationError
from app.responses.get import GetResponse
from app.controllers.get import GetController

get_router = APIRouter()


class KeyValidator(BaseModel):
    key: Any = Field(..., min_length=1, description="The key must be a non-empty object.")


@get_router.get(path="/")
async def get(request: Request)->GetResponse:
    payload = await request.json()
    try:
        data = KeyValidator(**payload)
    except ValidationError as e:
        return GetResponse(status_code=422, msg=e.errors())
    
    success, response = GetController.get(data.key)
    return GetResponse(
        status_code=response["status_code"],
        msg=response["message"],
        data=response.get("data") if success else None,
        timestamp=datetime.now().isoformat() if success else None
    )