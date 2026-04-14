import tkinter as tk


class Pantalla2(tk.Frame):
    def __init__(self, app):
        super().__init__(app.root)
        self.app = app

        self.entry = tk.Entry(self)
        self.entry.pack(pady=10)

        boton_volver = tk.Button(
            self, 
            text="Volver",
            command=self.volver
        )
        boton_volver.pack(pady=10)


    def volver(self):
        self.app.valor = self.entry.get()
        self.app.mostrar_pantalla1()