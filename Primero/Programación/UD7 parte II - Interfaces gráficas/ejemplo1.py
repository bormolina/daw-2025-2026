import tkinter as tk

class HolaMundoApp:
    def __init__(self, root):
        self.root = root

        self.root.title("Adios Mundo")
        self.root.geometry("1200x500")
        self.root.resizable(True, True)

        # Etiqueta de saludo
        self.label_saludo = tk.Label(
            self.root, 
            text="La NES tenía 2kb de RAM",
            font=("Arial", 30),
            fg="blue",
            bg="red"
        )
        
        # pack() coloca el widget en la ventana
        self.label_saludo.pack(pady=20)


# Ejecutar la app
if __name__ == "__main__":
    root = tk.Tk()
    app = HolaMundoApp(root)
    root.mainloop()