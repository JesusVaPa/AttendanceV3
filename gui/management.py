import tkinter as tk
from tkinter.font import Font
from tkinter import messagebox

class Management(tk.Frame):
    def __init__(self, parent):
        super().__init__(parent)

        def check_login():
            expected_username = "Pejman Azadi"
            expected_password = "Lasalle420"
            
            # Get the entered username and password
            entered_username = username_entry.get()
            entered_password = password_entry.get()
            
            # Check if the entered username and password match the expected values
            if entered_username == expected_username and entered_password == expected_password:
                messagebox.showinfo("Login", "Login Successful!")
                
            else:
                messagebox.showerror("Login", "Invalid username or password.")

        font_style_login = Font(family="Arial", size=15)

        # Create the username label and entry field
        username_label = tk.Label(self, bg="white", text="Username:", font=font_style_login)
        username_label.grid(row=1, column=0, columnspan=2, padx=650, pady=50)

        username_entry = tk.Entry(self, font=font_style_login, justify="center")
        username_entry.grid(row=2, column=0, columnspan=2, padx=650, pady=5)

        # Create the password label and entry field
        password_label = tk.Label(self, bg="white", text="Password:", font=font_style_login)
        password_label.grid(row=3, column=0, columnspan=2, padx=650, pady=50)

        password_entry = tk.Entry(self, show="*", font=font_style_login, justify="center")
        password_entry.grid(row=4, column=0, columnspan=2, padx=650, pady=5)

        # Create the submit button
        submit_button = tk.Button(self, text="Submit", font=font_style_login, command=check_login)
        submit_button.grid(row=5, column=0, columnspan=2, padx=650, pady=30)

      


