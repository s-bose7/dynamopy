from typing import Tuple

class Redis:
    
    def __init__(self) -> None:
        self.counter = 0

    def write(self, key, value)->Tuple[str]:
        self.counter += 1
        if self.counter%2 == 0:
            return "OK", "SUCCESS" 
        else:
            return "FAILED", "ERROR"
    

redis_db: Redis = Redis()