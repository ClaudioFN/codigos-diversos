'''
Created Date: 30/06/2024
Last Update: 29/03/2025
Description: Main class for the API (making imports from the others parts)
Observation: Class for the main part of the API and its calling
'''

from fastapi import FastAPI
from workout_api.routers import api_router

app = FastAPI(title='WorkoutApi')
app.include_router(api_router)


    
    