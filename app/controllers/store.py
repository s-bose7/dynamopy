from typing import Tuple, Dict, Any

from app.models.store import HeisenbergStore


class StoreController:
    
    def put(self, key: Any, value: Any)-> Tuple[bool, Dict[str, Any]]:
        MAX_KEY_LENGTH = 100
        # Serialized key
        if not isinstance(key, str):
            key = str(key)
        
        if len(key) > MAX_KEY_LENGTH:
            return False, {
                "status_code": 404, 
                "message":f"Client error, Key exceeds maximum length {self.MAX_KEY_LENGTH}"
            }

        return HeisenbergStore.put(key=key, value=value)
        
