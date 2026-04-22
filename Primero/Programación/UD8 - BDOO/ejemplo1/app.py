from ZODB import DB  # Clase principal de la base de datos
from ZODB.FileStorage import FileStorage  # Permite guardar la BD en un fichero
import transaction  # Gestión de transacciones (guardar cambios)
from datetime import datetime
from persistent import Persistent  # Para hacer objetos persistentes
from persistent.list import PersistentList  # Lista compatible con ZODB
import os


# Crear carpeta si no existe (para guardar la BD ahí)
os.makedirs("./ejemplo1", exist_ok=True)


class Item(Persistent):
    def __init__(self, nombre: str):
        self.nombre = nombre
        self.fecha_creacion = datetime.now()

    def __str__(self):
        return f"{self.nombre} (creado el {self.fecha_creacion.strftime('%d/%m/%Y %H:%M:%S')})"


# Configuración de la base de datos
storage = FileStorage("./ejemplo1/checklist.fs")  # Fichero donde se guarda la BD
db = DB(storage)  # Crear la BD
connection = db.open()  # Abrir conexión
root = connection.root()  # Objeto raíz (diccionario persistente)

# Inicializar la lista si no existe
if "items" not in root:
    root["items"] = PersistentList()


items = root["items"]  # Referencia a la lista de items


# Programa principal
while True:
    print("\n--- CHECKLIST ---")

    if items:
        for i, item in enumerate(items, start=1):  # Mostrar desde 1 (no desde 0)
            print(f"{i}. {item}")
    else:
        print("No hay items aún.")

    print("\n1) Nuevo item")
    print("0) Salir")

    opcion = input("Elige opción: ")

    if opcion == "1":
        nombre = input("Nombre del item: ")
        nuevo_item = Item(nombre)
        root["items"].append(nuevo_item)  # Añadir al root directamente
        transaction.commit()  # Guardar cambios en la BD
        print("Item añadido ✔")

    elif opcion == "0":
        print("Saliendo...")
        break

    else:
        print("Opción no válida")


# Cierre limpio
connection.close()  # Cerrar conexión
db.close()  # Cerrar BD
storage.close()  # Cerrar fichero