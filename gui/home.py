import tkinter as tk

class Home(tk.Frame):
    def __init__(self, parent):
        super().__init__(parent)

        # Widgets and components for Page One
        label = tk.Label(self, text="thuis is my home poag")
        label.pack(pady=20)

