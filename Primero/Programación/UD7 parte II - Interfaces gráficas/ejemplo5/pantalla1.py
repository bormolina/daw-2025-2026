import tkinter as tk


class Pantalla1(tk.Frame):
    def __init__(self, app):
        super().__init__(app.root)
        self.app = app

        self.label = tk.Label(self, text="")
        self.label.pack(pady=20)

        boton = tk.Button(self, text="Ir a pantalla 2", command=self.app.mostrar_pantalla2)
        boton.pack()

    def actualizar_label(self):
        self.label.config(text=self.app.valor)