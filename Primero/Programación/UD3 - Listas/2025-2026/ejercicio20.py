def imprimirMenu():
    print("1. Ver tareas pendientes")
    print("2. Agregar tarea")
    print("0. Salir")


def imprimirTareasPendientes(tareas: list[str]):
    separador = "------------"
    print(separador)
    for i, tarea in enumerate(tareas):
        print(f"{i+1}. {tarea}")
    print(separador)

def insertarTarea(tareas: list[str]) -> list[str]:
    nuevaTarea = input("Qué tarea quieres insertar? ")
    pos = int(input("En qué posición"))
    tareas.insert(pos-1, nuevaTarea)
    return tareas


tareas = ["Comprar fruta", "Estudiar programación", "Comprar skin de Amumu"]

print("Bienvenido a la app de to-do más avanzada del universo")

while True:
    imprimirMenu()
    opcion = input()

    if opcion == "0":
        break
    elif opcion == "1":
        imprimirTareasPendientes(tareas)
    elif opcion == "2":
        tareas = insertarTarea(tareas)
    else:
        print("Opción no valida")