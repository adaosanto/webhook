from core.config import settings

import sqlalchemy as sqa

class ValoresRecebidoModel(settings.DBModelBase):
    
    __tablename__ = 'valores_recebidos'

    id: int = sqa.Column(sqa.Integer, autoincrement=True, primary_key=True)
    valor_recebido: dict = sqa.Column(sqa.JSON, nullable=False)