from typing import Tuple, Dict, Any

from app.models.store import HeisenbergStore


class StoreController:

    def __init__(self) -> None:
        self.MAX_KEY_LENGTH = 100
        
    
    def put(self, key: Any, value: Any)-> Tuple[bool, Dict[str, Any]]:
        
        # Serialized key
        if not isinstance(key, str):
            key = str(key)
        
        if len(key) > self.MAX_KEY_LENGTH:
            return False, {
                "status_code": 404, 
                "message":f"Client error, Key exceeds maximum length {self.MAX_KEY_LENGTH}"
            }

        return HeisenbergStore.put(key=key, value=value)
        
