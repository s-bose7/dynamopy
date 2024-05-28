from typing import Tuple, Any

import os
import sys
from dotenv import load_dotenv

import redis


class Redis:
    
    def __init__(self) -> None:
        load_dotenv()        

        self.db = redis.Redis(
            host=os.getenv("HOST"),
            port=os.getenv("PORT"),
            password=None,
            # All responses are returned as bytes in Python. 
            # To receive decoded strings, set decode_responses=True. 
            decode_responses=True 
        )

    def write(self, key, value)->Tuple[str]:
        try:
            self.db.set(key, value)
        except Exception as e:
            return "NOT OK", e
        
        return "OK", "SUCCESS"


    def read(self, key)->Any:
        return self.db.get(key)


    def exists(self, key)->bool:
        return self.db.exists(key)
    

    def remove(self, key)->bool:
        pass


redis_db: Redis = Redis()