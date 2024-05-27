from typing import Dict, Any

from pydantic import BaseModel
from datetime import datetime
from fastapi import APIRouter, Request

from app.responses.store import StoreResponse
from app.controllers.store import StoreController


store_router = APIRouter()

class KeyValueValidator(BaseModel):
    key: Any
    value: Any  


# Store arbitrary key-value pairs, which can contain any type of data
# i.e. text, numbers, counters, characters and binary data
@store_router.post(path="/")
async def set(request: Request)-> StoreResponse:
    
    payload = await request.json()
    # Validate request
    kv = KeyValueValidator(**payload)
    
    success, response = StoreController.put(key=kv.key, value=kv.value)
    return StoreResponse(
        status_code=response["status_code"],
        message=response["message"],
        timestamp=None if not success else datetime.now().isoformat()
    )
