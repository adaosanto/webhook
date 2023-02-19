from fastapi import APIRouter

from api.v1.endpoints import usuario
from api.v1.endpoints import alvara

api_router = APIRouter()

api_router.include_router(usuario.router, prefix='/usuarios', tags=['usuarios'])
api_router.include_router(alvara.router, prefix='/alvaras', tags=['alvaras'])