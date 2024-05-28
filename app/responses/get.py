from typing import Dict, Any, Optional

from fastapi.responses import JSONResponse


class GetResponse(JSONResponse):
    def __init__(self, status_code: int, msg: str, data: Optional[Dict[str, Any]], timestamp: Optional[str]):
        response_content: Dict[str, Any] = {
            "status_code": status_code,
            "message": msg,
        }
        if data:
            response_content["data"] = data
        if timestamp:
            response_content["timestamp"]=timestamp 
        
        super().__init__(
            content=response_content,
            media_type="application/json"
        )
        