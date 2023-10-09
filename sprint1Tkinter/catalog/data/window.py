from tkinter import ttk
import tkinter as tk
from tkinter import messagebox
from cell import Cell

class MainWindow():
    def __init__(self, root):
        root.title("MainWindow")

        self.cells = [
            Cell("Mariposa1","C:\\msys64\\home\\maril\\nuevo\\DWES\\sprint1Tkinter\\catalog\\data\\unedited\\mariposa1.jpg"),
            Cell("Mariposa2","C:\\msys64\\home\\maril\\nuevo\\DWES\\sprint1Tkinter\\catalog\\data\\unedited\\mariposa2.jpg"),
            Cell("Mariposa3","C:\\msys64\\home\\maril\\nuevo\\DWES\\sprint1Tkinter\\catalog\\data\\unedited\\mariposa3.jpg"),
            Cell("Mariposa4","C:\\msys64\\home\\maril\\nuevo\\DWES\\sprint1Tkinter\\catalog\\data\\unedited\\mariposa4.jpg"),
            Cell("Mariposa5","C:\\msys64\\home\\maril\\nuevo\\DWES\\sprint1Tkinter\\catalog\\data\\unedited\\mariposa5.jpg"),
        ]

        for i, cell in enumerate(self.cells):
            label = ttk.Label(root, image=cell.image_tk, text=cell.title, compound=tk.BOTTOM)
            label.grid(row=1, column=i)
            label.bind("<Button-1>", lambda event, celda=cell: self.on_button_clicked(cell))

    def on_button_clicked(self, cell):
        message = "Mi Mariposuario " + cell.title
        messagebox.showinfo("Información", message)