import tkinter as tk
import datetime
from tkinter.font import Font
from database.course_model import Course_Model
from database.classes_attendance_model import Classes_Attendance_Model
from src.TrainingRF import train_model

class Attendance(tk.Frame):
    def __init__(self, parent):
        super().__init__(parent)

        self.status_text = tk.StringVar()

        font_style_start = Font(family="Arial", size=25)
        font_selection = Font(family="Arial", size=17)
        font_courses = Font(family="Arial", size=15)

        select_course_label = tk.Label(self, text="Please select the course:", font=font_selection)
        select_course_label.place(relx=0.5, rely=0.3, anchor="center")

        courses = Course_Model.getCourses()
        course_names = [course[1] for course in courses] 
        #print(course_names)

        # Create a variable to hold the selected course
        self.selected_course = tk.StringVar()
        self.selected_course.set(course_names[0])  # Set the default value to the first course

        # Create a dropdown menu for selecting the course
        dropdown_menu = tk.OptionMenu(self, self.selected_course, *course_names)
        dropdown_menu.config(font=font_courses)  # Apply the font style to the menu
        dropdown_menu["menu"].config(font=font_courses)  # Apply the font style to the options
        dropdown_menu.place(relx=0.5, rely=0.35, anchor="center")

        # Create a centered button for starting recognition
        button = tk.Button(self, text="START", bg="red", fg="white", font=font_style_start, command=self.start_recognition)
        button.place(relx=0.5, rely=0.5, anchor="center")
        tk.Label(self, textvariable=self.status_text, font=font_style_start).place(relx=0.5, rely=0.3, anchor="center")

    def start_recognition(self):
        selected_course = self.selected_course.get()
        self.status_text.set(f"Training the model for {selected_course}, please wait")
        names = train_model()  # Pass the selected course to the train_model function
        self.status_text.set('Recognition end')

        print('attendance' + str(names))
        current_date = datetime.date.today()
        for student_id in names:
            attendance = Classes_Attendance_Model(student_id, 1, current_date)
            attendance.postClassAttendance()
