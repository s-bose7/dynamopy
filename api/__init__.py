from fastapi import APIRouter

from .v1 import v1_router

router = APIRouter()
router.include_router(v1_router, prefix="/v1")


# If someone tries to import all names from this module using  
# `from api import *`, only the router object will be imported. 
# Other names defined in the module (i.e. v1_router) will not  
# be imported, unless they are explicitly referenced.
__all__ = ["router"]