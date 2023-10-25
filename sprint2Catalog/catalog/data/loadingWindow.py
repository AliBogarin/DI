
import threading
import requests
import tkinter as tk
from tkinter import ttk
from window import MainWindow


class LoadingWindow():
    def __init__(self, root):
        self.root = root
        self.finished = False
        self.json_data = []
        self.root.title("Cargando...")
        self.root.geometry("170x170") # Define el alto y el ancho

        #Ajusto la ventana en medio de la pantalla
        x=(self.root.winfo_screenwidth() - self.root.winfo_reqwidth())/2
        y=(self.root.winfo_screenheight() - self.root.winfo_reqheight())/2
        self.root.geometry(f"+{int(x)}+{int(y)}")

        self.root.resizable(False,False) # Indica si la ventana puede ser redimensionada o no

        self.label = tk.Label(self.root, text="Cargando datos...", font=("Arial", 14)) # Definimos tipo de fuente y tamaño
        self.label.pack(side=tk.TOP, pady=10)

        label_bg_color = self.label.cget("bg") # Nos permite obtener el valor de la fuente

        self.canvas = tk.Canvas(self.root,width=60, height=60, bg=label_bg_color)  # Con canvas pintaremos la circunferencia
        self.canvas.pack()

        self.progress = 0

        self.draw_progress_circle(self.progress)
        
        self.update_progress_circle()

        self.thread = threading.Thread(target=self.fetch_json_data)
        self.thread.start()

        if self.thread.is_alive():
            self.check_thread()

        
    def draw_progress_circle(self, progress):
        self.canvas.delete("progress")
        angle = int(360*(progress/100))

        # Dibuja la porción de progreso en verde
        self.canvas.create_arc (10, 10, 50, 50, start=0, extent=angle, tags="progress", outline='green', width=4, style=tk.ARC)
        
    def update_progress_circle(self):
        if self.progress < 100:
            self.progress += 12 #Aquí completamos el circulo
        else:
            self.progress = 0

        self.draw_progress_circle(self.progress)
        self.root.after(50,self.update_progress_circle) # Llama a la función update_progress_circle cada 50 milisegundos

    def fetch_json_data(self):
        response = requests.get("https://raw.githubusercontent.com/AliBogarin/DWES/main/recursos/catalog.json")
        if response.status_code == 200:
            self.json_data = response.json() # Llama a la función para lanzar la ventana principal
            self.finished = True

    #Verifica cada 100 milisegundos si ha terminado alguna tarea, destruye la ventana actual y abre otra nueva.
    def check_thread(self):
        if self.finished:
            self.root.destroy()
            self.launch_main_window(self.json_data)
        else:
            self.root.after(100, self.check_thread)
    #Lanza la  ventana principal
    def launch_main_window(self, json_data):
        root = tk.Tk()
        MainWindow(root,json_data)
        root.mainloop()