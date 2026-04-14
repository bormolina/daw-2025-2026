import tkinter as tk


class PantallaInicio(tk.Frame):
    def __init__(self, app):
        super().__init__(app.root)
        self.app = app

        self.boton_empezar = tk.Button(
            self,
            command=lambda: self.app.mostrar(self.app.p_juego),
            width=18
        )
        self.boton_empezar.pack(pady=20)

        self.boton_configurar = tk.Button(
            self,
            command=lambda: self.app.mostrar(self.app.p_config),
            width=18
        )
        self.boton_configurar.pack(pady=10)

    def actualizar(self):
        self.boton_empezar.config(text=self.app.t("inicio_empezar"))
        self.boton_configurar.config(text=self.app.t("inicio_configurar"))