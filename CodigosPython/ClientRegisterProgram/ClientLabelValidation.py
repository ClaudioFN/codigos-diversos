"""
Created Date: 30/03/2024
Last Update: 24/11/2024
Description: Labels to do the validation
"""
import tkinter as tk

class ClientLabelValidation: 

    def labels(window):
        label_cpf_cnpj = tk.Label(window)
        label_cpf_cnpj.grid(row=0, column=2)

        label_name = tk.Label(window)
        label_name.grid(row=1, column=2)

        label_address = tk.Label(window)
        label_address.grid(row=2, column=2)

        label_neighborhood = tk.Label(window)
        label_neighborhood.grid(row=3, column=2)

        label_city = tk.Label(window)
        label_city.grid(row=4, column=2)

        label_state = tk.Label(window)
        label_state.grid(row=5, column=2)

        label_fu = tk.Label(window)
        label_fu.grid(row=6, column=2)

        label_phones = tk.Label(window)
        label_phones.grid(row=9, column=1)
            