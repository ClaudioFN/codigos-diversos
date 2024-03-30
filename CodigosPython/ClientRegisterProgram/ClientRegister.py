"""
Created Date: 23/03/2024
Last Update: 29/03/2024
Description: Program to get the details of a person
"""
import tkinter as tk
from datetime import datetime
import os
from PIL import Image, ImageTk
from WriteFile import WriteFile
from ClientValidation import ClientValidation

date_format = datetime.today().strftime('%d-%m-%Y')
file_name = f'client-{date_format}.csv'
#regex_email = '^[a-z0-9]+[\._]?[a-z0-9]+[@]\w+[.]\w{2,3}$'


# To not substitute the file
def find(name, path):
    for root, dirs, files in os.walk(path):
        if name in files:
            return os.path.join(root, name)

window = tk.Tk()
window.geometry("320x250")
window.title("Client Register")

img = ImageTk.PhotoImage(Image.open('./python-powered-h-50x65.png'))
window.iconphoto(True, img)
tk.Label(window, image=img)

#Labels for the window Client Register
tk.Label(window, text="CPF/CNPJ:").grid(row=0, column=0, sticky="w")
tk.Label(window, text="Name:").grid(row=1, column=0, sticky="w")
tk.Label(window, text="Address").grid(row=2, column=0, sticky="w")
tk.Label(window, text="Neighborhood:").grid(row=3, column=0, sticky="w")
tk.Label(window, text="City:").grid(row=4, column=0, sticky="w")
tk.Label(window, text="State:").grid(row=5, column=0, sticky="w")
tk.Label(window, text="FU:").grid(row=6, column=0, sticky="w")
tk.Label(window, text="Main Phone:").grid(row=7, column=0, sticky="w")
tk.Label(window, text="Mobile Phone:").grid(row=8, column=0, sticky="w")

#Enter fields
entry_cpf_cnpj = tk.Entry(window)
entry_cpf_cnpj.grid(row=0, column=1)

label_cpf_cnpj = tk.Label(window, text="-")
label_cpf_cnpj.grid(row=0, column=2)

entry_name = tk.Entry(window)
entry_name.grid(row=1, column=1)

label_name = tk.Label(window, text="-")
label_name.grid(row=1, column=2)

entry_address = tk.Entry(window)
entry_address.grid(row=2, column=1)

label_address = tk.Label(window, text="-")
label_address.grid(row=2, column=2)

entry_neighborhood = tk.Entry(window)
entry_neighborhood.grid(row=3, column=1)

label_neighborhood = tk.Label(window, text="-")
label_neighborhood.grid(row=3, column=2)

entry_city = tk.Entry(window)
entry_city.grid(row=4, column=1)

label_city = tk.Label(window, text="-")
label_city.grid(row=4, column=2)

entry_state = tk.Entry(window)
entry_state.grid(row=5, column=1)

label_state = tk.Label(window, text="-")
label_state.grid(row=5, column=2)

entry_fu = tk.Entry(window)
entry_fu.grid(row=6, column=1)

label_fu = tk.Label(window, text="-")
label_fu.grid(row=6, column=2)

entry_main_phone = tk.Entry(window)
entry_main_phone.grid(row=7, column=1)

entry_mobile_phone = tk.Entry(window)
entry_mobile_phone.grid(row=8, column=1)

label_phones = tk.Label(window, text="-")
label_phones.grid(row=9, column=1)

def execution():
    error_required, client_details = ClientValidation.client_register(window, entry_cpf_cnpj, entry_name, entry_address, 
                                                                     entry_neighborhood, entry_city, entry_state, entry_fu, entry_main_phone, 
                                                                     entry_mobile_phone)
    anyFileFound = ''
    anyFileFound = find(file_name, os.getcwd())    

    if error_required != "S":
        WriteFile.file_editing(anyFileFound, file_name, 
                            ['CPF_CNPJ', 'NAME', 'ADDRESS', 'NEIGHBORHOOD', 'CITY', 'STATE', 'FU', 'MAIN_PHONE', 'MOBILE_PHONE'],
                            client_details)
    else:
        print('Error in one of the fields!')

# Register Button
button = tk.Button(window, text="Register", command = execution)
button.grid(row = 10, column = 1, pady = 10)

window.mainloop()