"""
Created Date: 05/05/2024
Last Update: 11/05/2024
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
        