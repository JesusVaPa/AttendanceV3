import tkinter as tk
from tkinter.font import Font
from tkinter import messagebox
from database.student_model import Student_Model
from src.FaceCapture import face_capture

class Students_List(tk.Frame):
       
    def update_students_list(self):
        self.remove_all_rows()
        all_students = Student_Model.getStudents()
        table_font = Font(family='Arial', size=15)
        
        for index, student in enumerate(all_students):
            tk.Label(self, text=student[0], font=table_font).grid(row=1 + index, column=4, padx=10, pady=4)  # Adjusted padx here
            tk.Label(self, text=student[2], font=table_font).grid(row=1 + index, column=5, padx=10, pady=4)  # Adjusted padx here
            tk.Label(self, text=student[1], font=table_font).grid(row=1 + index, column=6, padx=10, pady=4)  # Adjusted padx here
            tk.Label(self, text=student[3], font=table_font).grid(row=1 + index, column=7, padx=10, pady=4)  # Adjusted padx here
            #tk.Button(self, text="Edit", command="").grid(row=1 + index, column=8, padx=10, pady=10)
            tk.Button(self, text="Delete", font=table_font, fg='white', bg='#DE1717', command=lambda l=student[0]: self.delete_student(l)).grid(row=1 + index, column=9, padx=10, pady=10)
            folder_name = student[2] + '_' + student[1]
            tk.Button(self, text="Capture Face", font=table_font, fg='white', bg="#191970", command=lambda l=folder_name:face_capture(l)).grid(row=1 + index, column=10, padx=10, pady=10)
    
    def remove_all_rows(self):
        for row in range(1, 50):
            widgets_in_row = self.grid_slaves(row=row)
            for widget in widgets_in_row:
                widget.grid_forget()

    def delete_student(self, id):
        print(id)
        if Student_Model.deleteStudent(id):
            messagebox.showinfo("Success", "Student has been deleted successfully.")
            self.update_students_list()
        else:
            messagebox.showinfo("Error", "Student has not been deleted.")
    
    def __init__(self, parent):
        super().__init__(parent)

        column_font = Font(family='Arial', size=15)

        # table of students
        tk.Label(self, text="ID", font=column_font).grid(row=0, column=4, padx=10, pady=5)  # Adjusted padx here
        tk.Label(self, text="First Name", font=column_font).grid(row=0, column=5, padx=10, pady=5)  # Adjusted padx here
        tk.Label(self, text="Last Name", font=column_font).grid(row=0, column=6, padx=10, pady=5)  # Adjusted padx here
        tk.Label(self, text="Email", font=column_font).grid(row=0, column=7, padx=10, pady=5)  # Adjusted padx here
        tk.Label(self, text="Actions", font=column_font).grid(row=0, column=8, columnspan=2, padx=10, pady=5)  # Adjusted padx here

        self.update_students_list()

        