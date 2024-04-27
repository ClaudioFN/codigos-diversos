"""
Created Date: 23/03/2024
Last Update: 23/04/2024
Description: Program to get the details of a person
"""
import tkinter as tk
from tkinter import messagebox

import os
from PIL import Image, ImageTk
from WriteFile import WriteFile
from ClientValidation import ClientValidation
from ClientLabels import ClientLabels
import Config
from  ProgramLabels import ProgramLabels
from DatabaseConnection import DatabaseConnection as db

config_definitions = Config
program_labels = ProgramLabels
fields_names = [config_definitions.CPF_CNPJ_TEXT, config_definitions.NAME_TEXT, config_definitions.ADDRESS_TEXT, config_definitions.NEIGHBORHOOD_TEXT
              , config_definitions.CITY_TEXT, config_definitions.STATE_TEXT, config_definitions.FU_TEXT, config_definitions.MAIN_PHONE_TEXT
              , config_definitions.MOBILE_PHONE_TEXT]
#regex_email = '^[a-z0-9]+[\._]?[a-z0-9]+[@]\w+[.]\w{2,3}$'
selected_option = ['']

# To not substitute the file
def find(name, path):
    for root, dirs, files in os.walk(path):
        if name in files:
            return os.path.join(root, name)

def handle_click(event):
    selected_option.clear()
    selected_option.append(event.get())


window = tk.Tk()
window.geometry("350x290")
window.title("Client Register")

img = ImageTk.PhotoImage(Image.open(config_definitions.PROGRAM_LOGO))
window.iconphoto(True, img)
tk.Label(window, image=img)

# Radio Button selection for the place to save the data
v = tk.StringVar(window, config_definitions.SAVE_DATA)
v.trace_add(['read'], lambda name, index, mode, var=v: handle_click(v))


db_img   = ImageTk.PhotoImage(Image.open(config_definitions.DB_RADIO_BUTTON_IMAGE).resize((24,24)), size=(1,1))
csv_img  = ImageTk.PhotoImage(Image.open(config_definitions.CSV_RADIO_BUTTON_IMAGE).resize((24,24)), size=(1,1))
radio_button_db  = tk.Radiobutton(window, text="DB", variable=v, value="DB", image=db_img)
radio_button_csv = tk.Radiobutton(window, text="CSV", variable=v, value="CSV", image=csv_img)

tk.Label(window, text=f"{config_definitions.SAVE_LOCATION_TEXT}:").grid(row=0, column=0, sticky="w")

radio_button_db.grid(row=0, column=1)
radio_button_csv.grid(row=0, column=2)

#Labels for the window Client Register
for i, labels_availables in enumerate(fields_names):
    program_labels.program_labels_definition(window, labels_availables, i + 1)


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
    if error_required != "S" and selected_option[0] == 'DB':
        connection = db.db_connection()
        db.db_insert_data(connection, client_details)
        if connection:
            connection.close() 
    elif error_required != "S" and selected_option[0] == 'CSV':
        anyFileFound = ''
        anyFileFound = find(config_definitions.FILE_NAME, os.getcwd() + '/' + config_definitions.CSV_LOCATION)
        complete_path = os.path.join(os.getcwd() + '/' +config_definitions.CSV_LOCATION, config_definitions.FILE_NAME)
            
        WriteFile.file_editing(anyFileFound, complete_path, config_definitions.FILE_NAME, 
                            ['CPF_CNPJ', 'NAME', 'ADDRESS', 'NEIGHBORHOOD', 'CITY', 'STATE', 'FU', 'MAIN_PHONE', 'MOBILE_PHONE'],
                            client_details)
    else:
        print(f'Error in one of the fields! {selected_option[0]}')

# Register Button
button = tk.Button(window, text="Register", command = execution)
button.grid(row = 11, column = 1, pady = 10)

window.mainloop()