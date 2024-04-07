"""
Created Date: 23/03/2024
Last Update: 07/04/2024
Description: Create new labels for the main program
Methods: 
 1 - program_labels_definition: Make the new label
 1.1 - Enter parameters: tk_origin = Tk class variable | label_name = name of the label | row_number = number of the row
"""
import tkinter as tk

class ProgramLabels:
    def program_labels_definition(tk_origin, label_name, row_number):
        return tk.Label(tk_origin, text=f"{label_name}: ").grid(row=row_number, column=0, sticky="w")
