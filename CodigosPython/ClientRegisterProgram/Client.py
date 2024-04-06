"""
Created Date: 29/03/2024
Last Update: 03/04/2024
Description: Contains the details to register a client
"""

class Client:
    def __init__(self, cpf_cnpj, name, address, neighborhood, city, state, fu, main_phone, mobile_phone):
        self.cpf_cnpj = cpf_cnpj
        self.name = name
        self.address = address
        self.neighborhood = neighborhood
        self.city = city
        self.state = state
        self.fu = fu
        self.main_phone = main_phone
        self.mobile_phone = mobile_phone
