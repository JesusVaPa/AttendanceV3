import tkinter as tk
from tkinter import ttk
from tkinter.font import Font
from PIL import ImageTk, Image
import subprocess

def go_home():
    # Open the "Home.py" script in a new process and destroy the current window
    subprocess.Popen(["python", "Code\Home.py"])
    window.destroy()

def go_attendance():
    # Open the "Attendance.py" script in a new process and destroy the current window
    subprocess.Popen(["python", "Code\Attendance.py"])
    window.destroy()

def go_reports():
    # Open the "Reports.py" script in a new process and destroy the current window
    subprocess.Popen(["python", "Code\Reports.py"])
    window.destroy()

def go_management():
# Open the "Management.py" script in a new process and destroy the current window
    subprocess.Popen(["python", "Code\Management.py"])
    window.destroy()

def start_recognition():
    # Start the facial recognition script in a new process
    subprocess.Popen(["python", "Code\FacialRecognition.py"])

# Create the main window
window = tk.Tk()
window.title("My GUI")
window.configure(bg="white")

# Load the logo image
logo_image = tk.PhotoImage(file="Media/logo-lasalle-college-montreal.png")

# Create a label to display the logo
logo_label = tk.Label(window, image=logo_image, bg="white")
logo_label.grid(row=0, column=0, padx=10, pady=20)

# Create a frame for the navigation bar
navigation_frame = tk.Frame(window, bg="white")
navigation_frame.grid(row=0, column=1, padx=(300, 10), pady=20)

font_style = Font(family="Arial", size=16)
font_style_start = Font(family="Arial", size=25)
font_style_footer = Font(family="Arial", size=8)

home_button = tk.Button(navigation_frame, text="HOME", relief="flat", bg="white", highlightthickness=0, font=font_style, command=go_home)
home_button.grid(row=0, column=0, padx=30, pady=5)

attendance_button = tk.Button(navigation_frame, text="ATTENDANCE", relief="flat", bg="white", highlightthickness=0, font=font_style, command=go_attendance)
attendance_button.grid(row=0, column=1, padx=30, pady=5)

reports_button = tk.Button(navigation_frame, text="REPORTS", relief="flat", bg="white", highlightthickness=0, font=font_style, command=go_reports)
reports_button.grid(row=0, column=2, padx=30, pady=5)

management_button = tk.Button(navigation_frame, text="MANAGEMENT", relief="flat", bg="white", highlightthickness=0, font=font_style, command=go_management)
management_button.grid(row=0, column=3, padx=30, pady=5)

welcome_label = tk.Label(window, text=" ©2023 LCI Education ", font=font_style_footer, bg="white")
welcome_label.place(relx=0.46, rely=0.94)

# Create a centered button for starting recognition
button = tk.Button(window, text="START", font=font_style_start, command=start_recognition)
button.place(relx=0.5, rely=0.5, anchor="center")

# Configure the window as borderless fullscreen
window.attributes('-fullscreen', True)

# Start the main event loop
window.mainloop()
