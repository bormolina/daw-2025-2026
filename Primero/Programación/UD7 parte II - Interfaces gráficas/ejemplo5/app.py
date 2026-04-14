import tkinter as tk
from pantalla1 import Pantalla1
from pantalla2 import Pantalla2


class App:
    def __init__(self, root):
        self.root = root
        self.root.title("App con múltiples pantallas")
        self.root.geometry("300x200")

        # Estado compartido
        self.valor = "Valor inicial"

        # Pantallas
        self.pantalla1 = Pantalla1(self)
        self.pantalla2 = Pantalla2(self)

        self.mostrar_pantalla1()

    def mostrar_pantalla1(self):
        self.pantalla2.pack_forget() # Oculta la pantalla 2
        self.pantalla1.actualizar_label()
        self.pantalla1.pack(fill="both", expand=True)

    def mostrar_pantalla2(self):
        self.pantalla1.pack_forget() # Oculta la pantalla 1
        self.pantalla2.pack(fill="both", expand=True)


# Ejecutar
if __name__ == "__main__":
    root = tk.Tk()
    app = App(root)
    root.mainloop()