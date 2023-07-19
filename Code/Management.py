import tkinter as tk
from tkinter import messagebox
from tkinter.font import Font
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

def check_login():
    expected_username = "Pejman Azadi"
    expected_password = "Lasalle420"
    
    # Get the entered username and password
    entered_username = username_entry.get()
    entered_password = password_entry.get()
    
    # Check if the entered username and password match the expected values
    if entered_username == expected_username and entered_password == expected_password:
        messagebox.showinfo("Login", "Login Successful!")
        go_management() 
    else:
        messagebox.showerror("Login", "Invalid username or password.")

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
font_style_login = Font(family="Arial", size=15)

home_button = tk.Button(navigation_frame, text="HOME", relief="flat", bg="white", highlightthickness=0, font=font_style, command=go_home)
home_button.grid(row=0, column=0, padx=30, pady=5)

attendance_button = tk.Button(navigation_frame, text="ATTENDANCE", relief="flat", bg="white", highlightthickness=0, font=font_style, command=go_attendance)
attendance_button.grid(row=0, column=1, padx=30, pady=5)

reports_button = tk.Button(navigation_frame, text="REPORTS", relief="flat", bg="white", highlightthickness=0, font=font_style, command=go_reports)
reports_button.grid(row=0, column=2, padx=30, pady=5)

management_button = tk.Button(navigation_frame, text="MANAGEMENT", relief="flat", bg="white", highlightthickness=0, font=font_style, command=go_management)
management_button.grid(row=0, column=3, padx=30, pady=5)

# Create the username label and entry field
username_label = tk.Label(window, bg="white", text="Username:", font=font_style_login)
username_label.grid(row=1, column=0, columnspan=2, padx=10, pady=50)

username_entry = tk.Entry(window, font=font_style_login, justify="center")
username_entry.grid(row=2, column=0, columnspan=2, padx=10, pady=5)

# Create the password label and entry field
password_label = tk.Label(window, bg="white", text="Password:", font=font_style_login)
password_label.grid(row=3, column=0, columnspan=2, padx=10, pady=50)

password_entry = tk.Entry(window, show="*", font=font_style_login, justify="center")
password_entry.grid(row=4, column=0, columnspan=2, padx=10, pady=5)

# Create the submit button
submit_button = tk.Button(window, text="Submit", font=font_style_login, command=check_login)
submit_button.grid(row=5, column=0, columnspan=2, padx=10, pady=30)

# Configure the window as borderless fullscreen
window.attributes('-fullscreen', True)

# Run the GUI main loop
window.mainloop()
