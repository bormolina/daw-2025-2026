import json
import tkinter as tk

from pathlib import Path

from pantalla_inicio import PantallaInicio
from pantalla_juego import PantallaJuego
from pantalla_config import PantallaConfig


class App:
    def __init__(self, root):
        self.root = root
        self.root.title("App Dados")
        self.root.geometry("320x240")
        self.root.resizable(False, False)

        # Carga de datos externos
        self.textos = self.cargar_textos()
        self.config = self.cargar_config()

        # Pantallas
        self.p_inicio = PantallaInicio(self)
        self.p_juego = PantallaJuego(self)
        self.p_config = PantallaConfig(self)

        self.pantalla_actual = None
        self.mostrar(self.p_inicio)

    def cargar_textos(self):
        ruta = Path(__file__).parent / "textos.json"
        with open(ruta, "r", encoding="utf-8") as f:
            return json.load(f)

    def cargar_config(self):
        try:
            with open("config.json", "r", encoding="utf-8") as f:
                config = json.load(f)

            if "dado" not in config or "idioma" not in config:
                raise ValueError("Configuración incompleta")

            if config["idioma"] not in self.textos:
                raise ValueError("Idioma no válido")

            return config

        except Exception:
            return {"dado": 6, "idioma": "ES"}

    def guardar_config(self):
        ruta = Path(__file__).parent / "config.json"
        with open(ruta, "w", encoding="utf-8") as f:
            json.dump(self.config, f, ensure_ascii=False, indent=4)

    def t(self, clave):
        idioma = self.config["idioma"]
        return self.textos[idioma][clave]

    def mostrar(self, pantalla):
        if self.pantalla_actual is not None:
            self.pantalla_actual.pack_forget()

        if hasattr(pantalla, "actualizar"):
            pantalla.actualizar()

        if hasattr(pantalla, "cargar_valores"):
            pantalla.cargar_valores()

        self.pantalla_actual = pantalla
        self.pantalla_actual.pack(fill="both", expand=True)


if __name__ == "__main__":
    root = tk.Tk()
    app = App(root)
    root.mainloop()