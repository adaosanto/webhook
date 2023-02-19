from sqlalchemy.ext.asyncio import (
    AsyncSession,
    AsyncEngine,
    create_async_engine
)
from sqlalchemy.orm import sessionmaker
from core.config import settings
engine: AsyncEngine = create_async_engine(settings.DB_URL)
Session: AsyncSession = sessionmaker(
    class_=AsyncSession,
    bind=engine,
    autocommit=False,
    expire_on_commit=False,
    autoflush=False
)