import tkinter as tk
import requests
from io import BytesIO
from PIL import Image, ImageTk

class Cell:
    def __init__(self, title, description, url):
        ## Constructor.
        self.title = title
        self.description = description
        self.url = url

        ## Convertimos la url a imagen importando requests y BytesIO.
        response = requests.get(self.url)
        img_data = Image.open(BytesIO(response.content))
        self.image_tk = ImageTk.PhotoImage(img_data)
        
    def load_image_from_url(self, url):
        response = requests.get(url)
        img = Image.open(BytesIO(response.content))
        return img
    #git add sprint2Catalog para subir cambios, hacerlos desde DWES
    