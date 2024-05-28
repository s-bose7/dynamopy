from typing import Tuple, Any

class Redis:
    
    def __init__(self) -> None:
        self.counter = 0

    def write(self, key, value)->Tuple[str]:
        self.counter += 1
        if self.counter%2 == 0:
            return "OK", "SUCCESS" 
        else:
            return "FAILED", "ERROR"
        

    def read(self, key)->Any:
        pass

    def exists(self, key)->bool:
        pass


redis_db: Redis = Redis()