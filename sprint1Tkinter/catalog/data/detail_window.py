import tkinter as tk
from tkinter import ttk
from PIL import Image, ImageTk


class DetailWindow:
    def _init_(self, root, title, image, description):

        self.root = root
        self.title = title
        self.image = image
        self.description = description
        self.window = tk.Toplevel(root)
        self.window.title(self.title)

        image_label = ttk.Label(self.window, image = self.image)
        image_label.pack()
        title_label = ttk.Label(self.window, text = self.title, font=("Mi mariposuario ", 16))
        title_label.pack()
        description_label = ttk.Label(self.window, text = self.description, wraplength = 300)
        description_label.pack()

    def _load_image(self, image_path):
        img = Image.open(image_path)
        imagen_redimensionada = img.resize((100, 100), Image.Resampling.LANCZOS)
        return ImageTk.PhotoImage(imagen_redimensionada)