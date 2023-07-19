import tkinter as tk

class Attendance(tk.Frame):
    def __init__(self, parent):
        super().__init__(parent)

        # Widgets and components for Page One
        label = tk.Label(self, text="Attendance")
        label.pack(pady=20)

