"""
Created Date: 05/05/2024
Last Update: 05/05/2024
Description: Create new window for the program
"""
import tkinter as tk
from PIL import Image, ImageTk

class ProgramWindow:
    def create_window():
        window = tk.Tk()
        window.geometry("350x290")
        window.title("Client Register")
        return window

    def create_window_logo(tk_window, program_logo):
        img = ImageTk.PhotoImage(Image.open(program_logo))
        tk_window.iconphoto(True, img)
        tk.Label(tk_window, image=img)
    
    def create_buttons_w_logo(tk_window, program_icon_image, program_icon_name, default_value_definition, position):
        icon_image = ImageTk.PhotoImage(Image.open(program_icon_image).resize((24,24)), size=(1,1))
        button_created = tk.Radiobutton(tk_window, text=program_icon_name, variable=default_value_definition, value=program_icon_name, image=icon_image)
        button_created.grid(row=0, column=position)
        