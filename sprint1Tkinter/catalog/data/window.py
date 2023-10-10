from tkinter import ttk
import tkinter as tk
from tkinter import messagebox
from cell import Cell
from detail_window import DetailWindow

class MainWindow():
        
    def on_button_clicked(self, cell):
        DetailWindow(self.root, cell.title, cell.imageTk, cell.description)

    def __init__(self, root):
        root.title("Mi Mariposuario")

        self.cells = [
            Cell("Morpho peleides","C:\\msys64\\home\\maril\\nuevo\\DWES\\sprint1Tkinter\\catalog\\data\\unedited\\mariposa1.jpg","La mariposa Morpho Azul (Morpho peleides) es una de las mariposas más grandes del mundo, con una envergadura de hasta 8 pulgadas de largo. Estas mariposas se encuentran en América Central y del Sur, y son las mariposas más comunes del género Morpho en América Central."),
            Cell("Appias","C:\\msys64\\home\\maril\\nuevo\\DWES\\sprint1Tkinter\\catalog\\data\\unedited\\mariposa2.jpg","Appias albina, el albatros común, es una pequeña mariposa de la familia Pieridae. Se encuentra en el sur y sureste de Asia a Australia"),
            Cell("Polyommatus icarus","C:\\msys64\\home\\maril\\nuevo\\DWES\\sprint1Tkinter\\catalog\\data\\unedited\\mariposa3.jpg","La mariposa ícaro se encuentra ampliamente distribuida por toda Europa, incluidas las islas mediterráneas, Asia templada y norte de África. En Macaronesia sólo aparece en las Islas Canarias."),
            Cell("Heliconius","C:\\msys64\\home\\maril\\nuevo\\DWES\\sprint1Tkinter\\catalog\\data\\unedited\\mariposa4.jpg","Esta mariposa diurna es bastante conocida en todo el mundo, ya que fue declarada mariposa oficial del Estado de Florida en el año 1996. Podemos verla desde el nivel del mar hasta los 1.800 metros de altitud."),
            Cell("Hypolimnas bolina","C:\\msys64\\home\\maril\\nuevo\\DWES\\sprint1Tkinter\\catalog\\data\\unedited\\mariposa5.jpg","Hypolimnas bolina , la gran mosca del huevo, la mosca común o en Nueva Zelanda la mariposa luna azul es una especie de mariposa ninfalida que se encuentra desde Madagascar hasta Asia y Australia."),
        ]

        for i, cell in enumerate(self.cells):
            label = ttk.Label(root, image=cell.image_tk, text=cell.title, compound=tk.BOTTOM)
            label.grid(row=1, column=i)
            label.bind("<Button-1>", self._make_on_button_clicked(cell))

    def _make_on_button_clicked(self, cell):
        return lambda event: self.on_button_clicked(cell)

    def on_button_clicked(self, cell):
        message = "Mi Mariposuario " + cell.description
        messagebox.showinfo("Información", message)