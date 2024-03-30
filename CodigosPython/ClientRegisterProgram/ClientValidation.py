"""
Created Date: 30/03/2024
Last Update: 30/03/2024
Description: Validate the data inserted
"""
import Client
import tkinter as tk

class ClientValidation: 
    # Format the person document
    def doc_format(cpf_cnpj_typed):
        doc_after_format = ""
        cpf_cnpj_typed = cpf_cnpj_typed.replace(".", "").replace("/","").replace("-","")
        
        if len(cpf_cnpj_typed) <= 11:
            cpf_cnpj_typed = cpf_cnpj_typed.rjust(11, "0")
            doc_after_format = '{}.{}.{}-{}'.format(cpf_cnpj_typed[:3], cpf_cnpj_typed[3:6],
                                                    cpf_cnpj_typed[6:9], cpf_cnpj_typed[9:]) 
        else:
            cpf_cnpj_typed = cpf_cnpj_typed.rjust(14, "0")
            doc_after_format = '{}.{}.{}/{}-{}'.format(cpf_cnpj_typed[:2],
                                                    cpf_cnpj_typed[2:5],
                                                    cpf_cnpj_typed[5:8],
                                                    cpf_cnpj_typed[8:12],
                                                    cpf_cnpj_typed[12:14])
        return doc_after_format  

    # Validation of the fields
    def client_register(window, entry_cpf_cnpj, entry_name, entry_address, entry_neighborhood, entry_city, entry_state, entry_fu, entry_main_phone, entry_mobile_phone):
        client_details = Client
        error_required = "N"
        
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
        
        
        if entry_cpf_cnpj.get():
            client_details.cpf_cnpj = ClientValidation.doc_format(entry_cpf_cnpj.get())

            label_cpf_cnpj.config(
                text="-",
                foreground="black",
            )                                 
        else:
            label_cpf_cnpj.config(
                text="Required",
                foreground="red",
            )   
            error_required = "S"
        
        if entry_name.get():                          
            client_details.name = entry_name.get()
            label_name.config(
                text="-",
                foreground="black",
            ) 
        else:
            label_name.config(
                text="Required",
                foreground="red",
            )   
            error_required = "S"
            
        if entry_address.get():   
            client_details.address = entry_address.get()
            label_address.config(
                text="-",
                foreground="black",
            )
        else:
            label_address.config(
                text="Required",
                foreground="red",
            )   
            error_required = "S"
        
        if entry_neighborhood.get():     
            client_details.neighborhood = entry_neighborhood.get()
            label_neighborhood.config(
                text="-",
                foreground="black",
            )
        else:
            label_neighborhood.config(
                text="Required",
                foreground="red",
            )
            error_required = "S"
        
        if entry_city.get():   
            client_details.city = entry_city.get()
            label_city.config(
                text="-",
                foreground="black",
            )
        else:
            label_city.config(
                text="Required",
                foreground="red",
            )
            error_required = "S"
    
        if entry_state.get():         
            client_details.state = entry_state.get()
            label_state.config(
                text="-",
                foreground="black",
            )
        else:
            label_state.config(
                text="Required",
                foreground="red",
            )
            error_required = "S"
    
        if entry_fu.get():      
            client_details.fu = entry_fu.get()
            label_fu.config(
                text="-",
                foreground="black",
            )
        else:
            label_fu.config(
                text="Required",
                foreground="red",
            )
            error_required = "S"
        
        client_details.main_phone = entry_main_phone.get()
        client_details.mobile_phone = entry_mobile_phone.get()
        
        if not client_details.main_phone and not client_details.mobile_phone:
            label_phones.config(
                text="One of the Phones is Required",
                foreground="red",
            )
            error_required = "S"
            client_details.main_phone = "-" 
            client_details.mobile_phone = "-" 
        else:
            label_phones.config(
                text="-",
                foreground="black",
            )
            
        if not client_details.main_phone:
            client_details.main_phone = "-" 
        elif not client_details.mobile_phone:
            client_details.mobile_phone = "-" 
        
        return error_required, client_details