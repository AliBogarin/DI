from tkinter import  ttk
from yes_window import show_yes_window
from no_window import show_no_window

class MainWindow:
    def on_button_click(self):
        pass
    def __init__(self, root):
        self.root = root

        self.frame = ttk.Frame(self.root)
        self.frame.pack()

        self.label = ttk.Label(self.frame, text = "Voy a aprobar todo??")
        self.label.pack()

        self.boton = ttk.Button(self.frame,text="No", command=show_no_window)
        self.boton.pack(side="right")

        self.boton = ttk.Button(self.frame, text="Si",  command=show_yes_window)
        self.boton.pack(side="left")

"""      self.button = ttk.Button(self.frame, text = "OK", command = self.on_button_click)
        self.button.pack() """