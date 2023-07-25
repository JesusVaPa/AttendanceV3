import tkinter as tk
from tkinter import messagebox
from tkinter.font import Font
import re
from database.student_model import Student_Model
from students_list import Students_List

class Students_Edit(tk.Frame):
    def on_save(self):
        id = self.entry_id.get()
        first_name = self.entry_first_name.get()
        last_name = self.entry_last_name.get()
        email = self.entry_email.get()

        # Email validation using regular expression
        email_pattern = r'^[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}$'
        if not re.match(email_pattern, email):
            messagebox.showerror("Invalid Email", "Please enter a valid email address.")
            return

        myStudent = Student_Model(first_name, last_name, email)
        Student_Model.updateStudent(myStudent, id)
        messagebox.showinfo("Success", "Student has been updated successfully.")
        self.list_students()

    def remove_all_rows(self):
        for row in range(7, 50):
            widgets_in_row = self.grid_slaves(row=row)
            for widget in widgets_in_row:
                if isinstance(widget, tk.Radiobutton): # Verifica se é um radio button
                    widget.destroy()
    
    def on_radio_click(self):
        selected_option = self.radio_var.get()
        selected_student = Student_Model.getStudentByID(selected_option)
        self.entry_id.set(selected_student[0][0])
        self.entry_last_name .set(selected_student[0][1])
        self.entry_first_name.set(selected_student[0][2])
        self.entry_email.set(selected_student[0][3])


    def list_students(self):
        self.remove_all_rows()
        all_students = Student_Model.getStudents()
        
        for index, student in enumerate(all_students):
            name = student[2] + ' ' + student[1]
            tk.Radiobutton(self, text=name, variable=self.radio_var, value=student[0], command=self.on_radio_click).grid(row=7 + index, column=0, columnspan=2, padx=10, pady=5)


    def __init__(self, parent):
        super().__init__(parent)

        self.radio_var = tk.StringVar()
        self.entry_id = tk.StringVar()
        self.entry_first_name = tk.StringVar()
        self.entry_last_name = tk.StringVar()
        self.entry_email = tk.StringVar()

# Create Labels
    #Edit student Form

        column_font = Font(family='Arial', size=15)

        tk.Label(self, font=column_font, text="Edit Student").grid(row=0, column=0, columnspan=2, padx=10, pady=5)
        tk.Label(self, font=column_font, text="ID:").grid(row=1, column=0, padx=10, pady=5)
        tk.Label(self, font=column_font, text="First Name:").grid(row=2, column=0, padx=10, pady=5)
        tk.Label(self, font=column_font, text="Last Name:").grid(row=3, column=0, padx=10, pady=5)
        tk.Label(self, font=column_font, text="Email:").grid(row=4, column=0, padx=10, pady=5)


# Create Entry fields
        self.id_show = tk.Label(self, textvariable=self.entry_id).grid(row=1, column=1, padx=10, pady=5)
        self.first_name_entry = tk.Entry(self, font=column_font, textvariable=self.entry_first_name, justify="center")
        self.last_name_entry = tk.Entry(self, font=column_font, textvariable=self.entry_last_name, justify="center")
        self.email_entry = tk.Entry(self, font=column_font, textvariable=self.entry_email, justify="center")
        self.first_name_entry.grid(row=2, column=1, padx=10, pady=5)
        self.last_name_entry.grid(row=3, column=1, padx=10, pady=5)
        self.email_entry.grid(row=4, column=1, padx=10, pady=5)

# Create Save button
        tk.Button(self, font=column_font, text="Save", bg='#3fde31', command=self.on_save).grid(row=5, column=0, columnspan=2, padx=10, pady=10)
        tk.Label(self, font=column_font, text="All Students").grid(row=6, column=0, columnspan=2, padx=10, pady=5)

        self.list_students()