import tkinter as tk

class HolaMundoApp:
    def __init__(self, root):
        self.root = root

        self.root.title("Hola Mundo")
        self.root.geometry("300x100")
        self.root.resizable(True, True)

        # Etiqueta de saludo
        self.label_saludo = tk.Label(self.root, text="¡Hola, mundo!", font=("Arial", 18))
        
        # pack() coloca el widget en la ventana
        self.label_saludo.pack(pady=20)


# Ejecutar la app
if __name__ == "__main__":
    root = tk.Tk()
    app = HolaMundoApp(root)
    root.mainloop()