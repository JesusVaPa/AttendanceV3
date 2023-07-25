import tkinter as tk
import subprocess
from tkinter.font import Font
from src.TrainingRF import train_model

class Attendance(tk.Frame):
    def __init__(self, parent):
        super().__init__(parent)

        self.status_text = tk.StringVar()

        font_style_start = Font(family="Arial", size=25)
# Create a centered button for starting recognition
        button = tk.Button(self, text="START", bg="red", fg="white", font=font_style_start, command=self.start_recognition)
        button.place(relx=0.5, rely=0.5, anchor="center")
        tk.Label(self, textvariable=self.status_text, font=font_style_start).place(relx=0.5, rely=0.3, anchor="center")
    
    def start_recognition(self):
        self.status_text.set("Training the model, please wait")
        names = train_model()
        self.status_text.set('Recognition end')
        print('attendance' + str(names))
 


        


