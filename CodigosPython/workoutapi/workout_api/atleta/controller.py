from fastapi import APIRouter, status, Body

from workout_api.contrib.dependencies import DataBaseDependency
from workout_api.atleta.schemas import AtletaIn
router = APIRouter()

@router.post(path='/', summary='Criar Novo Atleta', status_code=status.HTTP_201_CREATED)
async def post(db_session: DataBaseDependency, atleta_in: AtletaIn = Body(...)):
    pass

