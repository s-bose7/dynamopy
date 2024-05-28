from typing import Dict, Tuple, Any

from core.database.redis import redis_db

class HeisenbergGet:

    @staticmethod
    def get(key: str)->Tuple[bool, Dict[str, Any]]:
        # Check if the key exists in the Redis database
        if not redis_db.exists(key):
            # If key is not present, return an error response
            return False, {
                "status_code": 404, 
                "message":f"Key '{key}' not found."
            }
        
        value = redis_db.read(key)
        data = {"key": key, "value": value}
        return True, {
            "status_code": 200, 
            "data": data,
            "message": "success"
        }