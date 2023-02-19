from pydantic import BaseModel

from sqlalchemy.ext.declarative import declarative_base

class Settings(BaseModel):

    DBModelBase = declarative_base()

    JWT_SECRET: str = 'Dw3-jfe6HIZFT8saj8xSFqeYSdAppp7UrOzIQBy2zg8'

    ALGORITHM: str = 'HS256'

    DB_URL: str = 'postgresql+asyncpg://postgres:dev@localhost:5432/postgres'

    API_V1_STR: str = '/v1/api'

    ACCESS_TOKEN_EXPIRE_MINUTES: int = 60 * 24 * 7

settings = Settings()