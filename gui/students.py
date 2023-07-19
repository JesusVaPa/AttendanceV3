import tkinter as tk
from tkinter import messagebox
import re
from data.database.student import Student

class Students(tk.Frame):
    def __init__(self, parent):
        super().__init__(parent)

# Create Labels
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

    def on_save(self):
        first_name = self.first_name_entry.get()
        last_name = self.last_name_entry.get()
        email = self.email_entry.get()

        # Email validation using regular expression
        email_pattern = r'^[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}$'
        if not re.match(email_pattern, email):
            messagebox.showerror("Invalid Email", "Please enter a valid email address.")
            return

        myStudent = Student(first_name, last_name, email)
        Student.postStudent(myStudent)

        messagebox.showinfo("Success", "Form data has been saved successfully.")
