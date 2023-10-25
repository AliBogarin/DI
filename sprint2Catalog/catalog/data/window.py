from logging import root
from tkinter import ttk
import tkinter as tk

from cell import Cell
from detail_window import DetailWindow



class MainWindow():

    def on_button_clicked(self, cell):
        DetailWindow(cell)

    def __init__(self, root, json_data):
        root.title("Mi Mariposuario")
        self.cells = [] # Inicializo una lista vacia de cell

        for i in json_data: #recorro cada cell
            name = i.get("name")
            description = i.get("description")
            url = i.get("image_url")
            
            self.cells.append(Cell(name, description, url))


        for i, cell in enumerate(self.cells): #Recorro cada cell en la lista
            label = ttk.Label(root, image=cell.image_tk, text=cell.title, compound=tk.BOTTOM)
            label.grid(row=i, column=0)
            label.bind("<Button-1>", lambda event, cell=cell: self.on_button_clicked(cell))


        width = int(180)
        height = int(400)
    
        root.geometry(str(width)+"x"+str(height))
    
        x=(root.winfo_screenwidth() - width)/2
        y=(root.winfo_screenheight() -height)/2
        root.geometry(f"+{int(x)}+{int(y)}")

   # def _make_on_button_clicked(self, cell):
   #     return lambda : self.on_button_clicked(cell)