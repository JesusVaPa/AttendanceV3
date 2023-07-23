import tkinter as tk
from tkinter import messagebox
import re
from database.student_model import Student_Model
from tkinter.font import Font
from student_add import Students_Add
from students_list import Students_List

pages = [
    {"label": "All Students", "frame": Students_List},
    {"label": "Add new Student", "frame": Students_Add}
]
class Students(tk.Frame):

    def __init__(self, parent):
        super().__init__(parent)

        self.current_frame = None
        # Create font styles
        font_buttons = Font(family="Arial", size=15)

        # Create a container frame for the buttons
        container = tk.Frame(self)
        container.grid(sticky="nsew")
        self.grid_rowconfigure(0, weight=1)
        self.grid_columnconfigure(0, weight=1)

        # Create the navigation bar frame
        nav_bar = tk.Frame(container, bg="white")
        nav_bar.grid(row=0, column=0, sticky="ew")

        # Create navigation buttons
        tk.Button(nav_bar, text="All Students", relief="flat", bg="white", font=font_buttons, command=lambda l="All Students": self.on_button_click(l)).grid(row=0, column=1, padx=10, pady=10)
        tk.Button(nav_bar, text="Add new Student", relief="flat", bg="white", font=font_buttons, command=lambda l="Add new Student": self.on_button_click(l)).grid(row=0, column=2, padx=10, pady=10)


        # Create the image frame (bottom part)
        image_frame = tk.Frame(container)
        image_frame.grid(row=1, column=0, columnspan=2, sticky="nsew")
        image_frame.grid_rowconfigure(0, weight=1)
        image_frame.grid_columnconfigure(0, weight=1)

        self.frames = {}
        for page in pages:
            label = page["label"]
            frame_class = page["frame"]
            self.frames[label] = frame_class(image_frame)
        
        # Show the first frame initially  
        self.show_frame("All Students")

    def on_button_click(self, label):
        self.show_frame(label)

    def show_frame(self, label):
        Students_List.update_students_list(self.frames["All Students"])
        if self.current_frame:
            self.current_frame.grid_forget()
        self.current_frame = self.frames[label]
        self.current_frame.grid(row=0, column=0, sticky="nsew")
            

           