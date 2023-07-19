import tkinter as tk
from PIL import Image, ImageTk
from students import Students
from home import Home
from attendance import Attendance

#inform here all pages that you want to show.
pages = [
        {"label": "Home", "frame": Home},
        {"label": "Students", "frame": Students},
        {"label": "Attendance", "frame": Attendance}
        ]

class App(tk.Tk):
    def __init__(self):
        super().__init__()
        self.title("Attendance APP")

# Set the size of the frame to match the screen resolution
        screen_width = self.winfo_screenwidth()
        screen_height = self.winfo_screenheight()
        self.geometry(f"{screen_width}x{screen_height}")

# Create the navigation bar frame
        nav_bar = tk.Frame(self, bg="blue")
        nav_bar.pack(side=tk.TOP, fill=tk.X)

    # Create navigation buttons  
        self.buttons = self.create_buttons(nav_bar, pages)
        for button in self.buttons:
            button.pack(side=tk.LEFT, padx=10, pady=5)

# Create the image frame (bottom part)
        image_frame = tk.Frame(self)
        image_frame.pack(side=tk.TOP, fill=tk.BOTH, expand=True)

        self.frames = {}
        for page in pages:
            label = page["label"]
            frame_class = page["frame"]
            self.frames[label] = frame_class(image_frame)

    # Show the first frame initially
        self.current_frame = None
        self.show_frame("Home")

    def create_buttons(self, parent, buttons_data):
        buttons = []
        for button_data in buttons_data:
            label = button_data["label"]
            button = tk.Button(parent, text=label, command=lambda l=label: self.on_button_click(l))
            buttons.append(button)
        return buttons

    def on_button_click(self, label):
        self.show_frame(label)

    def show_frame(self, label):
        if self.current_frame:
            self.current_frame.pack_forget()
        self.current_frame = self.frames[label]
        self.current_frame.pack(fill=tk.BOTH, expand=True)

if __name__ == "__main__":
    app = App()
    app.mainloop()