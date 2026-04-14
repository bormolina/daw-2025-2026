import random
import tkinter as tk


class PantallaJuego(tk.Frame):
    def __init__(self, app):
        super().__init__(app.root)
        self.app = app

        self.label = tk.Label(self, text="", font=("Arial", 16))
        self.label.pack(pady=20)

        self.boton_tirar = tk.Button(self, command=self.tirar, width=18)
        self.boton_tirar.pack(pady=10)

        self.boton_volver = tk.Button(
            self,
            command=lambda: self.app.mostrar(self.app.p_inicio),
            width=18
        )
        self.boton_volver.pack(pady=10)

    def actualizar(self):
        self.label.config(text=self.app.t("juego_pulsa"))
        self.boton_tirar.config(text=self.app.t("juego_tirar"))
        self.boton_volver.config(text=self.app.t("juego_volver"))

    def tirar(self):
        caras = self.app.config["dado"]
        resultado = random.randint(1, caras)

        texto = self.app.t("juego_resultado").format(
            resultado=resultado,
            caras=caras
        )
        self.label.config(text=texto)