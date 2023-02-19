from core.config import settings
import sqlalchemy as sqa

class UsuarioModel(settings.DBModelBase):
    
    __tablename__ = 'usuarios'

    id: int = sqa.Column(sqa.Integer, autoincrement=True, primary_key=True)
    nome: str = sqa.Column(sqa.String(256), nullable=True)
    sobrenome: str = sqa.Column(sqa.String(256), nullable=True)
    email: str = sqa.Column(sqa.String(256), nullable=False, index=True, unique=True)
    senha: str = sqa.Column(sqa.String(256), nullable=False)
