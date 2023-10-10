from PIL import Image, ImageTk
from detail_window import DetailWindow
from tkinter import messagebox
from tkinter import ttk
import tkinter as tk

class Cell:
    def __init__(self, title, image_path, description):
        self.title = title
        self.image_path = image_path
        self.description = description  # Añadido nuevo atributo de descripción
        self.image_tk = self._load_image(image_path)
        

    def _load_image(self, image_path):
        img = Image.open(image_path)
        imagen_redimensionada = img.resize((100, 100), Image.Resampling.LANCZOS)
        return ImageTk.PhotoImage(imagen_redimensionada)
    
    def on_button_clicked(self):
        DetailWindow(self.title, self.image_path, self.description)  # Modificado para usar el atributo de descripción