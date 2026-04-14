import tkinter as tk


class PantallaConfig(tk.Frame):
    def __init__(self, app):
        super().__init__(app.root)
        self.app = app

        self.label_dado = tk.Label(self)
        self.label_dado.pack(pady=(15, 5))

        self.entry_dado = tk.Entry(self, justify="center")
        self.entry_dado.pack()

        self.label_idioma = tk.Label(self)
        self.label_idioma.pack(pady=(15, 5))

        self.idioma_var = tk.StringVar()

        self.opciones_idioma = ["ES", "EN"]

        self.menu_idioma = tk.OptionMenu(self, self.idioma_var, *self.opciones_idioma)
        self.menu_idioma.pack()

        self.boton_guardar = tk.Button(self, command=self.guardar, width=18)
        self.boton_guardar.pack(pady=15)

        self.boton_volver = tk.Button(
            self,
            command=lambda: self.app.mostrar(self.app.p_inicio),
            width=18
        )
        self.boton_volver.pack()

    def cargar_valores(self):
        self.entry_dado.delete(0, tk.END)
        self.entry_dado.insert(0, str(self.app.config["dado"]))
        self.idioma_var.set(self.app.config["idioma"])
        self.actualizar()

    def actualizar(self):
        self.label_dado.config(text=self.app.t("config_titulo_dado"))
        self.label_idioma.config(text=self.app.t("config_titulo_idioma"))
        self.boton_guardar.config(text=self.app.t("config_guardar"))
        self.boton_volver.config(text=self.app.t("config_volver"))

        menu = self.menu_idioma["menu"]
        menu.delete(0, "end")

        opciones = [
            ("ES", self.app.t("idioma_es")),
            ("EN", self.app.t("idioma_en"))
        ]

        for codigo, texto_visible in opciones:
            menu.add_command(
                label=texto_visible,
                command=lambda c=codigo: self.idioma_var.set(c)
            )

    def guardar(self):
        try:
            dado = int(self.entry_dado.get())

            if dado <= 0:
                return

            self.app.config["dado"] = dado
            self.app.config["idioma"] = self.idioma_var.get()
            self.app.guardar_config()
            self.app.mostrar(self.app.p_inicio)

        except ValueError:
            pass