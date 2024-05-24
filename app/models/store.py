from typing import Tuple, Dict, Any
from core.database.redis import redis_db


class HeisenbergStore:

    def put(self, key: str, value: Any)-> Tuple[bool, Dict[str, Any]]:
        status, result = redis_db.write(key, value)

        if status != "OK":
            return False, {"status_code": 500, "message": result}
        
        return True, {"status_code": 200, "message": result}