from tkinter import Tk

# Importa la clase LoadingWindow desde el archivo loadingWindow.py
from loadingWindow import LoadingWindow

if __name__ == "__main__":
    root =Tk()
    app = LoadingWindow(root)
    root.mainloop()