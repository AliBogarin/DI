import tkinter as tk
import requests
from io import BytesIO
from PIL import Image, ImageTk

class Cell:
    def __init__(self, title, description, url):
        ## Constructor.
        self.title = title
        self.descrition = description
        self.url = url

        ## Convertimos la url a imagen importando requests y BytesIO.
        response = requests.get(self.url)
        img_data = Image.open(BytesIO(response.content))
        self.image_tk = ImageTk.PhotoImage(img_data)
        
        