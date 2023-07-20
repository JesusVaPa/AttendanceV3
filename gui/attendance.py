import tkinter as tk
import subprocess
from tkinter.font import Font

class Attendance(tk.Frame):
    def __init__(self, parent):
        super().__init__(parent)

        def start_recognition():
# Start the facial recognition script in a new process
            subprocess.Popen(["python", "src/FacialRecognition.py"])

        font_style_start = Font(family="Arial", size=25)
# Create a centered button for starting recognition
        button = tk.Button(self, text="START", bg="red", fg="white", font=font_style_start, command=start_recognition)
        button.place(relx=0.5, rely=0.5, anchor="center")
      
        

        


