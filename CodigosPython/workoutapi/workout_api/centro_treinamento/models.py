'''
Created Date: 30/06/2024
Last Update: 16/03/2025
Description: Class for models in the program
Observation: Class for the single model
'''
from contrib.models import BaseModel

from sqlalchemy import Integer, String
from sqlalchemy.orm import Mapped, mapped_column, relationship


class CentroTreinamentoModel(BaseModel):
    __tablename__ = 'centros_treinamento'
    
    pk_id: Mapped[int] = mapped_column(Integer, primary_key=True)
    nome: Mapped[str] = mapped_column(String(50), unique=True, nullable=False)
    endereco: Mapped[str] = mapped_column(String(60), nullable=False)
    proprietario: Mapped[str] = mapped_column(String(30), nullable=False)
    
    atleta: Mapped['AtletaModel'] = relationship(back_populates='centro_treinamento')