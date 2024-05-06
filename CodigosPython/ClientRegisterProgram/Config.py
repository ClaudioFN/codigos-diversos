"""
Created Date: 06/04/2024
Last Update: 05/05/2024
Description: Contains details of constants
"""
from datetime import datetime
import os

# Fields Sizes for Validation
CPF_CNPJ_SIZE = 14
NAME_SIZE = 25
ADDRESS_SIZE = 50
NEIGHBORHOOD_SIZE = 30
CITY_SIZE = 20
STATE_SIZE = 14
FU_SIZE = 2
MAIN_PHONE_SIZE = 11
MOBILE_PHONE_SIZE = 11

# Fields Names
CPF_CNPJ_TEXT = 'CPF/CNPJ'
NAME_TEXT = 'Name'
ADDRESS_TEXT = 'Address'
NEIGHBORHOOD_TEXT = 'Neighborhood'
CITY_TEXT = 'City'
STATE_TEXT = 'State'
FU_TEXT = 'FU'
MAIN_PHONE_TEXT = 'Main Phone'
MOBILE_PHONE_TEXT = 'Mobile Phone'
SAVE_LOCATION_TEXT = 'Save location'
DB_TEXT = 'DB'
CSV_TEXT = 'CSV'

# Default save operation
SAVE_DATA = 'DB' # DB | CSV

# Images location
DB_RADIO_BUTTON_IMAGE = './ClientRegisterProgram/images/icons8-search-database-50.png'
CSV_RADIO_BUTTON_IMAGE = './ClientRegisterProgram/images/icons8-csv-24.png'
PROGRAM_LOGO = './ClientRegisterProgram/images/python-powered-h-50x65.png'

# File location
CSV_LOCATION = '/ClientRegisterProgram/CSV-Files/'

# File name
FILE_NAME = f'client-{datetime.today().strftime('%d-%m-%Y')}.csv'

# Database Name
DB_NAME = 'mydatabase.db'
DB_LOCATION = os.getcwd() + '/ClientRegisterProgram/SQLiteStudio/'