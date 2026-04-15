import tkinter as tk


class CalculadoraApp:
    def __init__(self, root):
        self.root = root
        self.expresion = ""

        self.root.title("Calculadora")
        self.root.geometry("300x400")
        self.root.resizable(False, False)

        self.entrada = tk.Entry(
            self.root, 
            font=("Arial", 20), 
            justify="right", 
            bd=5,   # border width
            relief=tk.RIDGE # Tipo de borde (puede ser RAISED, SUNKEN, GROOVE, RIDGE)
        )
        self.entrada.pack(fill="both", padx=10, pady=10)

        botones = [
            ["7", "8", "9", "/"],
            ["4", "5", "6", "*"],
            ["1", "2", "3", "-"],
            ["0", "C", "=", "+"]
        ]

        boton_frame = tk.Frame(self.root)
        boton_frame.pack(
            expand=True, # Hace que el frame ocupe todo el espacio disponible
            fill="both", 
            padx=10, 
            pady=10
        )

        # Configuración de filas y columnas
        for i in range(4):
            boton_frame.rowconfigure(i, weight=1)
            boton_frame.columnconfigure(i, weight=1)

        # Creación dinámica de botones
        for i, fila in enumerate(botones):
            for j, texto in enumerate(fila):
                b = tk.Button(
                    boton_frame,
                    text=texto,
                    font=("Arial", 18),
                    command=lambda t=texto: self.pulsar(t) # al pulsar el botón, se llama a self.pulsar con el texto del botón como argumento
                )
                b.grid(row=i, column=j, sticky="nsew", padx=1, pady=1) # sticky="nsew" hace que el botón se expanda en todas las direcciones para llenar la celda de la cuadrícula

    def pulsar(self, tecla):
        if tecla == "C":
            self.expresion = ""
        elif tecla == "=":
            try:
                self.expresion = str(eval(self.expresion)) # Uso eval por motivos de simplicidad, pero en una aplicación real se debería usar un método más seguro para evaluar la expresión
            except Exception:
                self.expresion = "ERROR"
        else:
            self.expresion += tecla

        self.actualizar_entrada()

    def actualizar_entrada(self):
        self.entrada.delete(0, tk.END) # Elimina el texto actual de la entrada
        self.entrada.insert(0, self.expresion) # Inserta el nuevo texto (la expresión actualizada) en la entrada


# Ejecutar la app
if __name__ == "__main__":
    root = tk.Tk()
    app = CalculadoraApp(root)
    root.mainloop()