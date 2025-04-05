'''
Created Date: 30/06/2024
Last Update: 29/04/2025
Description: Router class
Observation: Class for the definition of the paths of router
'''

from fastapi import APIRouter
from workout_api.atleta.controller import router as atleta

api_router = APIRouter()
api_router.include_router(atleta, prefix='/atletas', tags=['atletas'])


