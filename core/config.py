from enum import Enum
from pydantic_settings import BaseSettings


class EnvironmentType(str, Enum):
    DEVELOPMENT = "development"
    PRODUCTION = "production"
    TEST = "test"

    
class BaseConfig(BaseSettings):
    class Config:
        case_sensitive = True


class Config(BaseConfig):
    DEBUG: int = 0
    DEFAULT_LOCALE: str = "en_US"
    ENVIRONMENT: str = EnvironmentType.DEVELOPMENT
    RELEASE_VERSION: str = "1.0"
    # DB_CONTAINER_IP_ADDRESS = "IPAddress"
    # MONGODB_URL: str =  f"mongodb://<{DB_CONTAINER_IP_ADDRESS}>:27017/"

config: Config = Config()