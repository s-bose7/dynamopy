from typing import Dict, Any
from datetime import datetime
from fastapi.responses import JSONResponse


class StoreResponse(JSONResponse):
    def __init__(self, status_code: int, message: str, timestamp: str = None):
        
        response_content: Dict[str, Any] = {
            "status_code": status_code,
            "message": message,
        }
        # Only add for successfull requests
        if timestamp is not None:
            response_content["timestamp"]=timestamp 

        super().__init__(
            content=response_content,
            media_type="application/json"
        )