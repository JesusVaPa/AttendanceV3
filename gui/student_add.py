import tkinter as tk
from tkinter import messagebox
import re
from database.student_model import Student_Model
from students_list import Students_List

class Students_Add(tk.Frame):
    def on_save(self):
        first_name = self.first_name_entry.get()
        last_name = self.last_name_entry.get()
        email = self.email_entry.get()

        # Email validation using regular expression
        email_pattern = r'^[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}$'
        if not re.match(email_pattern, email):
            messagebox.showerror("Invalid Email", "Please enter a valid email address.")
            return

        myStudent = Student_Model(first_name, last_name, email)
        Student_Model.postStudent(myStudent)

        messagebox.showinfo("Success", "Student has been saved successfully.")
        Students_List.update_students_list

    def __init__(self, parent):
        super().__init__(parent)

# Create Labels
    #new student Form
        tk.Label(self, text="First Name:").grid(row=0, column=0, padx=10, pady=5)
        tk.Label(self, text="Last Name:").grid(row=1, column=0, padx=10, pady=5)
        tk.Label(self, text="Email:").grid(row=2, column=0, padx=10, pady=5)


# Create Entry fields
        self.first_name_entry = tk.Entry(self)
        self.last_name_entry = tk.Entry(self)
        self.email_entry = tk.Entry(self)
        self.first_name_entry.grid(row=0, column=1, padx=10, pady=5)
        self.last_name_entry.grid(row=1, column=1, padx=10, pady=5)
        self.email_entry.grid(row=2, column=1, padx=10, pady=5)

# Create Save button
        tk.Button(self, text="Save", command=self.on_save).grid(row=3, column=0, columnspan=2, padx=10, pady=10)