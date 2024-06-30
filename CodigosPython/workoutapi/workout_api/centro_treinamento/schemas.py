from typing import Annotated

from pydantic import Field
from workoutapi.workout_api.contrib.schemas import BaseSchema


class CentroTreinamento(BaseSchema):
    nome: Annotated[str, Field(description='Nome do Centro de Treinamento', example='CT 1', max_length=20)]
    endereco: Annotated[str, Field(description='Endereco do Centro de Treinamento', example='Rua 1', max_length=60)]
    proprietario: Annotated[str, Field(description='Proprietario do Centro de Treinamento', example='Lucas', max_length=30)]