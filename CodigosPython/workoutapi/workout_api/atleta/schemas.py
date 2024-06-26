from typing import Annotated
from pydantic import Field, PositiveFloat

from workout_api.contrib.schemas import BaseSchema, OutMixin

class Atleta(BaseSchema):
    nome: Annotated[str, Field(description='Nome do Atleta', example='Juca', max_length=50)]
    cpf: Annotated[str, Field(description='CPF do Atleta', example='12312312312', max_length=11)]
    idade: Annotated[int, Field(description='Idade do Atleta', example=25)]
    peso: Annotated[PositiveFloat, Field(description='Peso do Atleta', example=75.75)]
    altura: Annotated[PositiveFloat, Field(description='Altura do Atleta', example=1.75)]
    sexo: Annotated[str, Field(description='Sexo do Atleta', example='M', max_length=1)]

class AtletaIn(Atleta):
    pass

class AtletaOut(AtletaIn, OutMixin):
    pass 