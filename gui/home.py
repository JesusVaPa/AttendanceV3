import tkinter as tk
from PIL import ImageTk, Image

class Home(tk.Frame):
    def __init__(self, parent):
        super().__init__(parent)

        self.welcome_image = Image.open("assets/imgs/background.jpg")
        # Resize the image proportionally to fit the screen width
        screen_width = self.winfo_screenwidth()
        aspect_ratio = self.welcome_image.width / self.welcome_image.height
        new_width = screen_width
        new_height = int(screen_width / aspect_ratio)
        self.welcome_image = self.welcome_image.resize((new_width, new_height))
        self.welcome_image = ImageTk.PhotoImage(self.welcome_image)

        # Create a label to display the image
        welcome_label = tk.Label(self, image=self.welcome_image, bg="white")
        welcome_label.place(relx=0, rely=0)
