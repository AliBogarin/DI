import threading
import tkinter as tk
from tkinter import ttk

class LoadingWindow():
    def __init__(self, root):
        self.root = root
        self.root.title("Cargando...")
        self.root.geometry("170x170") # Define el alto y el ancho
        self.root.resizable(False,False) # Indica si la ventana puede ser redimensionada o no

        self.label = tk.Label(self.root, text="Cargando datos...", font=("Arial", 14)) # Definimos tipo de fuente y tamaño
        self.label.pack(side=tk.TOP, pady=10)

        label_bg_color = self.label.cget("bg") # Nos permite obtener el valor de la fuente

        self.canvas = tk.Canvas(self.root,width=60, height=60, bg=label_bg_color)  # Con canvas pintaremos la circunferencia
        self.canvas.pack()

        self.progress = 0

        self.draw_progress_circle(self.progress)
        
        self.update_progress_circle()

        

        
    def draw_progress_circle(self, progress):
        self.canvas.delete("progress")
        angle = int(360*(progress / 100))

        # Dibuja la porción de progreso en verde
        self.canvas.create_arc (10, 10, 50, 50,
                                start=0, extent=angle, tags="progress", outline='green', width=4, style=tk.ARC)
        
    def update_progress_circle(self):
        if self.progress < 100:
            self.progress += 1 #Aquí completamos el circulo
        else:
            self.progress = 0

        self.draw_progress_circle(self.progress)
        self.root.after(50,self.update_progress_circle) # Llama a la función update_progress_circle cada 50 milisegundos

