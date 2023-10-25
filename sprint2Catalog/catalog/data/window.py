from logging import root
from tkinter import ttk
import tkinter as tk
from tkinter import messagebox
from cell import Cell
from detail_window import DetailWindow



class MainWindow():

    def on_button_clicked(self, cell):
        DetailWindow(cell)

    def acerca_de(self):
        messagebox.showinfo("Acerca del desarrollador", "Este programa fue desarrollado por Alicia.")

        

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

        
        menubar = tk.Menu(root)
        ayuda_menu = tk.Menu(menubar, tearoff=False)
        ayuda_menu.add_command(label="Acerca de", command=self.acerca_de)
        menubar.add_cascade(label="Ayuda", menu=ayuda_menu)

        root.config(menu=menubar)

        width = int(180)
        height = int(400)
    
        root.geometry(str(width)+"x"+str(height))
    
        x=(root.winfo_screenwidth() - width)/2
        y=(root.winfo_screenheight() -height)/2
        root.geometry(f"+{int(x)}+{int(y)}")

        

