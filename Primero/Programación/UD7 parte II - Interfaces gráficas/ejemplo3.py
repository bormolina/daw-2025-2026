import tkinter as tk

class ConversorApp:
    def __init__(self, root):
        self.root = root

        self.root.title("Conversor Km a Millas")
        self.root.geometry("800x600")

        # Etiqueta de instrucción
        self.label_info = tk.Label(
            self.root,
            text="Introduce kilómetros:", 
            font=("Arial", 30)
        )
        self.label_info.pack(pady=5)

        # Campo de entrada
        self.entry_km = tk.Entry(self.root, font=("Arial", 30))
        self.entry_km.pack(pady=5)

        # Botón de conversión
        self.boton_convertir = tk.Button(
            self.root, text="Convertir", 
            command=self.convertir,
            font=("Arial", 30)
        )
        self.boton_convertir.pack(pady=10)

        # Resultado
        self.label_resultado = tk.Label(self.root, text="")
        self.label_resultado.pack(pady=5)

    def convertir(self):
        km_texto = self.entry_km.get()

        try:
            km = float(km_texto)
            millas = km * 0.621371
            self.label_resultado.config(text=f"{millas:.2f} millas", font=("Arial", 30))
        except ValueError:
            self.label_resultado.config(text="Introduce un número válido")


# Ejecutar la app
if __name__ == "__main__":
    root = tk.Tk()
    app = ConversorApp(root)
    root.mainloop()