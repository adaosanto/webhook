from typing import Optional
from typing import List

from fastapi import APIRouter
from fastapi import HTTPException
from fastapi import status
from fastapi import Depends
from fastapi import Query
from fastapi import Response
from fastapi import Request
from fastapi.responses import JSONResponse

from sqlalchemy.future import select
from sqlalchemy.ext.asyncio import AsyncSession
from sqlalchemy.exc import IntegrityError

from models.usuario_model import UsuarioModel
from models.recebidos_webhook import ValoresRecebidoModel
from schemas.usuario_schema import *
from core.deps import get_current_user, get_session

router = APIRouter()


@router.post('/webhook', status_code=status.HTTP_202_ACCEPTED)
async def webhook(request: Request, db: AsyncSession = Depends(get_session), token = Depends(get_current_user)):
    try:
        payload = await request.json()
    
        novo_valor = ValoresRecebidoModel(valor_recebido=payload)
        if payload:
            db.add(novo_valor)
            await db.commit()
        return payload
        return Response(status_code=status.HTTP_202_ACCEPTED)
    except:
        return Response(status_code=status.HTTP_202_ACCEPTED)

@router.get('/recebidos')
async def valores(db: AsyncSession = Depends(get_session), token = Depends(get_current_user)):
    async with db as session:
        query = select(ValoresRecebidoModel)
        result = await session.execute(query)
        valores = result.scalars().all()

        return valores
