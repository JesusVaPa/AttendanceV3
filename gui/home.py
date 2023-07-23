import tkinter as tk
from PIL import ImageTk, Image

class Home(tk.Frame):
    def __init__(self, parent):
        super().__init__(parent)

        self.welcome_image = Image.open("assets/imgs/background.jpg")
        self.welcome_image = self.welcome_image.resize((1580, 650))
        self.welcome_image = ImageTk.PhotoImage(self.welcome_image)

        # Create a label to display the image
        welcome_label = tk.Label(self, image=self.welcome_image, bg="white")
        welcome_label.place(relx=-0.01, rely=0)
        


        
       