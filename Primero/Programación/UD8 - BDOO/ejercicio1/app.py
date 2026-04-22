from ZODB import DB
from ZODB.FileStorage import FileStorage
import transaction
from datetime import datetime
from persistent import Persistent
from persistent.list import PersistentList


class Item(Persistent):
    def __init__(self, nombre: str):
        self.nombre = nombre
        self.fecha_creacion = datetime.now()
        self.fecha_modificacion = self.fecha_creacion  # nueva: fecha de última modificación

    def __str__(self):
        return f"{self.nombre} (creado: {self.fecha_creacion.strftime('%d/%m/%Y %H:%M:%S')} | modificado: {self.fecha_modificacion.strftime('%d/%m/%Y %H:%M:%S')})"


storage = FileStorage("./ejercicio1/checklist.fs")
db = DB(storage)
connection = db.open()
root = connection.root()

if "items" not in root:
    root["items"] = PersistentList()

items = root["items"]


while True:
    print("\n--- CHECKLIST ---")

    if items:
        for i, item in enumerate(items, start=1):
            print(f"{i}. {item}")
    else:
        print("No hay items aún.")

    print("\n1) Nuevo item")
    print("0) Salir")
    print("(-x para borrar, m-x para modificar)")  # nuevo: explicación de opciones

    opcion = input("Elige opción: ")

    if opcion == "1":
        nombre = input("Nombre del item: ")
        nuevo_item = Item(nombre)
        root["items"].append(nuevo_item)
        transaction.commit()
        print("Item añadido ✔")

    elif opcion.startswith("-"):  # nuevo: borrar item
        try:
            indice = int(opcion[1:]) - 1
            if 0 <= indice < len(items):
                items.pop(indice)
                root["items"] = items
                transaction.commit()
                print("Item borrado ✔")
            else:
                print("Índice no válido")
        except:
            print("Formato incorrecto. Usa -x")

    elif opcion.startswith("m-"):  # nuevo: modificar item
        try:
            indice = int(opcion[2:]) - 1
            if 0 <= indice < len(items):
                nuevo_nombre = input("Nuevo nombre: ")
                items[indice].nombre = nuevo_nombre
                items[indice].fecha_modificacion = datetime.now()  # nueva: actualizar fecha
                transaction.commit()
                print("Item modificado ✔")
            else:
                print("Índice no válido")
        except:
            print("Formato incorrecto. Usa m-x")

    elif opcion == "0":
        print("Saliendo...")
        break

    else:
        print("Opción no válida")


connection.close()
db.close()
storage.close()