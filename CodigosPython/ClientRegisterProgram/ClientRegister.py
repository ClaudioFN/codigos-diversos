"""
Created Date: 23/03/2024
Last Update: 06/04/2024
Description: Program to get the details of a person
"""
import tkinter as tk
from tkinter import messagebox
from datetime import datetime
import os
from PIL import Image, ImageTk
from WriteFile import WriteFile
from ClientValidation import ClientValidation
from ClientLabels import ClientLabels
import Config

date_format = datetime.today().strftime('%d-%m-%Y')
file_name = f'client-{date_format}.csv'
config_definitions = Config
#regex_email = '^[a-z0-9]+[\._]?[a-z0-9]+[@]\w+[.]\w{2,3}$'


# To not substitute the file
def find(name, path):
    for root, dirs, files in os.walk(path):
        if name in files:
            return os.path.join(root, name)

window = tk.Tk()
window.geometry("350x290")
window.title("Client Register")

img = ImageTk.PhotoImage(Image.open('./ClientRegisterProgram/images/python-powered-h-50x65.png'))
window.iconphoto(True, img)
tk.Label(window, image=img)

# Radio Button selection for the place to save the data
var = ""
db_img   = ImageTk.PhotoImage(Image.open('./ClientRegisterProgram/images/icons8-search-database-50.png').resize((24,24)), size=(1,1))
csv_img  = ImageTk.PhotoImage(Image.open('./ClientRegisterProgram/images/icons8-csv-24.png').resize((24,24)), size=(1,1))
radio_button_db  = tk.Radiobutton(window, text="DB", variable=var, value="DB", image=db_img)
radio_button_csv = tk.Radiobutton(window, text="CSV", variable=var, value="CSV", image=csv_img)
tk.Label(window, text="Save location:").grid(row=0, column=0, sticky="w")

radio_button_db.grid(row=0, column=1)
radio_button_csv.grid(row=0, column=2)

#Labels for the window Client Register
tk.Label(window, text=f"{config_definitions.CPF_CNPJ_TEXT}: ").grid(row=1, column=0, sticky="w")
tk.Label(window, text=f"{config_definitions.NAME_TEXT}: ").grid(row=2, column=0, sticky="w")
tk.Label(window, text=f"{config_definitions.ADDRESS_TEXT}: ").grid(row=3, column=0, sticky="w")
tk.Label(window, text=f"{config_definitions.NEIGHBORHOOD_TEXT}: ").grid(row=4, column=0, sticky="w")
tk.Label(window, text=f"{config_definitions.CITY_TEXT}: ").grid(row=5, column=0, sticky="w")
tk.Label(window, text=f"{config_definitions.STATE_TEXT}: ").grid(row=6, column=0, sticky="w")
tk.Label(window, text=f"{config_definitions.FU_TEXT}: ").grid(row=7, column=0, sticky="w")
tk.Label(window, text=f"{config_definitions.MAIN_PHONE_TEXT}: ").grid(row=8, column=0, sticky="w")
tk.Label(window, text=f"{config_definitions.MOBILE_PHONE_TEXT}: ").grid(row=9, column=0, sticky="w")

def show_warning(limit_size, field_name):
    messagebox.showwarning('Warning', f'The Limit for {field_name} is {limit_size}')

warning_button = tk.Button(window, text="Show Warning", command=show_warning)
def char_count_validation(event):
    count_cpf_cnpj = len(entry_cpf_cnpj.get())
    count_name = len(entry_name.get())
    count_address = len(entry_address.get())
    count_neighborhood = len(entry_neighborhood.get())
    count_city = len(entry_city.get())
    count_state = len(entry_state.get()) 
    count_fu = len(entry_fu.get()) 
    count_main_phone = len(entry_main_phone.get()) 
    count_mobile_phone = len(entry_mobile_phone.get())
    if count_cpf_cnpj > config_definitions.CPF_CNPJ_SIZE and event.keysym not in {'BackSpace', 'Delete'}:
        show_warning(config_definitions.CPF_CNPJ_SIZE, config_definitions.CPF_CNPJ_TEXT)
        return 'break'  # dispose of the event, prevent typing
    if count_name > config_definitions.NAME_SIZE and event.keysym not in {'BackSpace', 'Delete'}:
        show_warning(config_definitions.NAME_SIZE, config_definitions.NAME_TEXT)
        return 'break'  # dispose of the event, prevent typing
    if count_address > config_definitions.ADDRESS_SIZE and event.keysym not in {'BackSpace', 'Delete'}:
        show_warning(config_definitions.ADDRESS_SIZE, config_definitions.ADDRESS_TEXT)
        return 'break'  # dispose of the event, prevent typing
    if count_neighborhood > config_definitions.NEIGHBORHOOD_SIZE and event.keysym not in {'BackSpace', 'Delete'}:
        show_warning(config_definitions.NEIGHBORHOOD_SIZE, config_definitions.NEIGHBORHOOD_TEXT)
        return 'break'  # dispose of the event, prevent typing
    if count_city > config_definitions.CITY_SIZE and event.keysym not in {'BackSpace', 'Delete'}:
        show_warning(config_definitions.CITY_SIZE, config_definitions.CITY_TEXT)
        return 'break'  # dispose of the event, prevent typing
    if count_state > config_definitions.STATE_SIZE and event.keysym not in {'BackSpace', 'Delete'}:
        show_warning(config_definitions.STATE_SIZE, config_definitions.STATE_TEXT)
        return 'break'  # dispose of the event, prevent typing
    if count_fu > config_definitions.FU_SIZE and event.keysym not in {'BackSpace', 'Delete'}:
        show_warning(config_definitions.FU_SIZE, config_definitions.FU_TEXT)
        return 'break'  # dispose of the event, prevent typing
    if count_main_phone > config_definitions.MAIN_PHONE_SIZE and event.keysym not in {'BackSpace', 'Delete'}:
        show_warning(config_definitions.MAIN_PHONE_SIZE, config_definitions.MAIN_PHONE_TEXT)
        return 'break'  # dispose of the event, prevent typing
    if count_mobile_phone > config_definitions.MOBILE_PHONE_SIZE and event.keysym not in {'BackSpace', 'Delete'}:
        show_warning(config_definitions.MOBILE_PHONE_SIZE, config_definitions.MOBILE_PHONE_TEXT)
        return 'break'  # dispose of the event, prevent typing

#Enter fields
entry_cpf_cnpj = tk.Entry(window)
entry_cpf_cnpj.grid(row=1, column=1)
entry_cpf_cnpj.bind('<KeyPress>', char_count_validation)

label_cpf_cnpj = tk.Label(window, text="-")
label_cpf_cnpj.grid(row=1, column=2)

entry_name = tk.Entry(window)
entry_name.grid(row=2, column=1)
entry_name.bind('<KeyPress>', char_count_validation)

label_name = tk.Label(window, text="-")
label_name.grid(row=2, column=2)

entry_address = tk.Entry(window)
entry_address.grid(row=3, column=1)
entry_address.bind('<KeyPress>', char_count_validation)

label_address = tk.Label(window, text="-")
label_address.grid(row=3, column=2)

entry_neighborhood = tk.Entry(window)
entry_neighborhood.grid(row=4, column=1)
entry_neighborhood.bind('<KeyPress>', char_count_validation)


label_neighborhood = tk.Label(window, text="-")
label_neighborhood.grid(row=4, column=2)

entry_city = tk.Entry(window)
entry_city.grid(row=5, column=1)
entry_city.bind('<KeyPress>', char_count_validation)

label_city = tk.Label(window, text="-")
label_city.grid(row=5, column=2)

entry_state = tk.Entry(window)
entry_state.grid(row=6, column=1)
entry_state.bind('<KeyPress>', char_count_validation)

label_state = tk.Label(window, text="-")
label_state.grid(row=6, column=2)

entry_fu = tk.Entry(window)
entry_fu.grid(row=7, column=1)
entry_fu.bind('<KeyPress>', char_count_validation)

label_fu = tk.Label(window, text="-")
label_fu.grid(row=7, column=2)

entry_main_phone = tk.Entry(window)
entry_main_phone.grid(row=8, column=1)
entry_main_phone.bind('<KeyPress>', char_count_validation)

entry_mobile_phone = tk.Entry(window)
entry_mobile_phone.grid(row=9, column=1)
entry_mobile_phone.bind('<KeyPress>', char_count_validation)

label_phones = tk.Label(window, text="-")
label_phones.grid(row=10, column=1)

client_labels = ClientLabels(label_cpf_cnpj, label_name, label_address, label_neighborhood, label_city, label_state, label_fu, label_phones)

def execution():
    error_required, client_details = ClientValidation.client_register_validation(window, client_labels, entry_cpf_cnpj, entry_name, entry_address, 
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
button.grid(row = 11, column = 1, pady = 10)

window.mainloop()