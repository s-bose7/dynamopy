from typing import Dict, Tuple, Any

from app.models.get import HeisenbergGet


class GetController:

    @staticmethod
    def get(key: Any)->Tuple[bool, Dict[str, Any]]:
        
        # serialization
        if not isinstance(key, str):
            key = str(key)
        
        return HeisenbergGet.get(key)
