import tkinter as tk
from PIL import ImageTk
from tkinter.font import Font
from home import Home
from students import Students
from attendance import Attendance
from management import Management


# Inform here all pages that you want to show.
pages = [
    {"label": "Home", "frame": Home},
    {"label": "Students", "frame": Students},
    {"label": "Attendance", "frame": Attendance},
    {"label": "Management", "frame": Management}
]

class App(tk.Tk):
    def __init__(self):
        super().__init__()
        self.title("Attendance APP")

        # Set the size of the frame to match the screen resolution
        screen_width = self.winfo_screenwidth()
        screen_height = self.winfo_screenheight()
        self.geometry(f"{screen_width}x{screen_height}")
        self.attributes('-fullscreen', True)

        # Create a container frame for the logo and buttons
        container = tk.Frame(self)
        container.grid(sticky="nsew")
        self.grid_rowconfigure(0, weight=1)
        self.grid_columnconfigure(0, weight=1)

        # Add a white stripe frame behind the logo
        logo_stripe = tk.Frame(container, bg="white", height=100)
        logo_stripe.grid(row=0, column=0, sticky="ew")

        # Load the logo image
        logo_image = ImageTk.PhotoImage(file="assets/imgs/logo.png")
        logo_label = tk.Label(logo_stripe, image=logo_image, bg="white")
        logo_label.image = logo_image
        logo_label.grid(padx=10, pady=10)

        # Create the navigation bar frame
        nav_bar = tk.Frame(container, bg="white")
        nav_bar.grid(row=0, column=1, sticky="ew")

        # Create font styles
        font_buttons = Font(family="Arial", size=20)

        # Create navigation buttons
        self.buttons = self.create_buttons(nav_bar, pages, font_buttons)
        for i, button in enumerate(self.buttons):
            button.grid(row=0, column=i, padx=10, pady=25)

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
        self.current_frame = None
        self.show_frame("Home")

        # Configure grid weights for responsive resizing
        container.grid_rowconfigure(1, weight=1)
        container.grid_columnconfigure(0, weight=1)
        container.grid_columnconfigure(1, weight=1)

        font_style_footer = Font(family="Arial", size=8)
        welcome_label = tk.Label(self, text=" ©2023 LCI Education ", font=font_style_footer)
        welcome_label.place(relx=0.46, rely=0.94)
        
    def create_buttons(self, parent, buttons_data, font_buttons):
        buttons = []
        for button_data in buttons_data:
            label = button_data["label"]
            button = tk.Button(parent, text=label, relief="flat", bg="white", font=font_buttons, command=lambda l=label: self.on_button_click(l))
            buttons.append(button)
        return buttons

    def on_button_click(self, label):
        self.show_frame(label)

    def show_frame(self, label):
        if self.current_frame:
            self.current_frame.grid_forget()
        self.current_frame = self.frames[label]
        self.current_frame.grid(row=0, column=0, sticky="nsew")
        
if __name__ == "__main__":
    app = App()
    app.mainloop()
