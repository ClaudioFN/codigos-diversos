"""
Created Date: 23/03/2024
Last Update: 11/05/2024
Description: Program to get the details of a person
"""
import tkinter as tk
import os
from PIL import Image, ImageTk
import Config
from ProgramLabelsEntries import ProgramLabelsEntries
from WriteFile import WriteFile
from ClientValidation import ClientValidation
from ClientLabels import ClientLabels
from Database import Database as db
from ProgramWindow import ProgramWindow as pw

config_definitions = Config
program_labels = ProgramLabelsEntries
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

# Create the window definition
window = pw.create_window()

# Create the association with the logo for the program
pw.create_window_logo(window, config_definitions.PROGRAM_LOGO)

# Radio Button selection for the place to save the data
v = tk.StringVar(window, config_definitions.SAVE_DATA)
v.trace_add(['read'], lambda name, index, mode, var=v: handle_click(v))

db_img   = ImageTk.PhotoImage(Image.open(config_definitions.DB_RADIO_BUTTON_IMAGE).resize((24,24)), size=(1,1))
csv_img  = ImageTk.PhotoImage(Image.open(config_definitions.CSV_RADIO_BUTTON_IMAGE).resize((24,24)), size=(1,1))
radio_button_db  = tk.Radiobutton(window, text="DB", variable=v, value="DB", image=db_img)
radio_button_csv = tk.Radiobutton(window, text="CSV", variable=v, value="CSV", image=csv_img)
radio_button_db.grid(row=0, column=1)
radio_button_csv.grid(row=0, column=2)

#Labels for the window Client Register
for i, labels_availables in enumerate(fields_names):
    program_labels.program_labels_definition(window, labels_availables, i + 1)

#Enter fields
tk.Label(window, text=f"{config_definitions.SAVE_LOCATION_TEXT}:").grid(row=0, column=0, sticky="w")

entry_cpf_cnpj = tk.Entry(window)
entry_cpf_cnpj.grid(row=1, column=1)
entry_cpf_cnpj.bind('<KeyPress>', lambda event: ClientValidation.char_count_validation(event, len(entry_cpf_cnpj.get()), config_definitions.CPF_CNPJ_TEXT, config_definitions.CPF_CNPJ_SIZE))

label_cpf_cnpj = tk.Label(window, text="-")
label_cpf_cnpj.grid(row=1, column=2)

entry_name = tk.Entry(window)
entry_name.grid(row=2, column=1)
entry_name.bind('<KeyPress>', lambda event: ClientValidation.char_count_validation(event, len(entry_name.get()), config_definitions.NAME_TEXT, config_definitions.NAME_SIZE))

label_name = tk.Label(window, text="-")
label_name.grid(row=2, column=2)

entry_address = tk.Entry(window)
entry_address.grid(row=3, column=1)
entry_address.bind('<KeyPress>', lambda event: ClientValidation.char_count_validation(event, len(entry_address.get()), config_definitions.ADDRESS_TEXT, config_definitions.ADDRESS_SIZE))

label_address = tk.Label(window, text="-")
label_address.grid(row=3, column=2)

entry_neighborhood = tk.Entry(window)
entry_neighborhood.grid(row=4, column=1)
entry_neighborhood.bind('<KeyPress>', lambda event: ClientValidation.char_count_validation(event, len(entry_neighborhood.get()), config_definitions.NEIGHBORHOOD_TEXT, config_definitions.NEIGHBORHOOD_SIZE))

label_neighborhood = tk.Label(window, text="-")
label_neighborhood.grid(row=4, column=2)

entry_city = tk.Entry(window)
entry_city.grid(row=5, column=1)
entry_city.bind('<KeyPress>', lambda event: ClientValidation.char_count_validation(event, len(entry_city.get()), config_definitions.CITY_TEXT, config_definitions.CITY_SIZE))

label_city = tk.Label(window, text="-")
label_city.grid(row=5, column=2)

entry_state = tk.Entry(window)
entry_state.grid(row=6, column=1)
entry_state.bind('<KeyPress>', lambda event: ClientValidation.char_count_validation(event, len(entry_state.get()), config_definitions.STATE_TEXT, config_definitions.STATE_SIZE))

label_state = tk.Label(window, text="-")
label_state.grid(row=6, column=2)

entry_fu = tk.Entry(window)
entry_fu.grid(row=7, column=1)
entry_fu.bind('<KeyPress>', lambda event: ClientValidation.char_count_validation(event, len(entry_fu.get()), config_definitions.FU_TEXT, config_definitions.FU_SIZE))

label_fu = tk.Label(window, text="-")
label_fu.grid(row=7, column=2)

entry_main_phone = tk.Entry(window)
entry_main_phone.grid(row=8, column=1)
entry_main_phone.bind('<KeyPress>', lambda event: ClientValidation.char_count_validation(event, len(entry_main_phone.get()), config_definitions.MAIN_PHONE_TEXT, config_definitions.MAIN_PHONE_SIZE))

entry_mobile_phone = tk.Entry(window)
entry_mobile_phone.grid(row=9, column=1)
entry_mobile_phone.bind('<KeyPress>', lambda event: ClientValidation.char_count_validation(event, len(entry_mobile_phone.get()), config_definitions.MOBILE_PHONE_TEXT, config_definitions.MOBILE_PHONE_SIZE))

label_phones = tk.Label(window, text="-")
label_phones.grid(row=10, column=1)

client_labels = ClientLabels(label_cpf_cnpj, label_name, label_address, label_neighborhood, label_city, label_state, label_fu, label_phones)

def execution():
    error_required, client_details = ClientValidation.client_register_required_items_validation(window, client_labels, entry_cpf_cnpj, entry_name, entry_address, 
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