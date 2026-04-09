from pathlib import Path
import random

# En estos ejercicios te recomiendo siempre crar una fucnión leer config que reciba la ruta del fichero de configuración y devuelva un diccionaro (o una tupla si hay pocos campos). En este caso como solo hay dos campos, devuelvo una tupla pero cuando hay más es mejor devolver un diccionario (sino te vas a tener un if-elif muy grande)
def leer_config(ruta: Path) -> tuple[str, int]:
    tipo_dado = "d6"
    num_tiradas = 1
    with open(ruta, "r", encoding="utf-8") as f:

        for linea in f:
            linea = linea.strip()
            if linea:
                partes = linea.split("=")
                clave = partes[0]
                valor = partes[1]

                if clave == "tipo_dado":
                    tipo_dado = valor
                elif clave == "num_tiradas":
                    num_tiradas = int(valor)

    return tipo_dado, num_tiradas


# De igual modo también te aconsejo crear una función para guardar la nueva configuración. El primer parámetros que siempre sea la ruta del fichero de configuración. El resto de parámetros que reciba la función dependerá de los campos que haya en la configuración, en este caso como solo hay dos campos, recibo dos parámetros pero si hubiera más, lo mejor sería recibir un diccionario con toda la configuración.
def guardar_config(ruta: Path, tipo_dado: str, num_tiradas: int) -> None:
    with open(ruta, "w", encoding="utf-8") as f:
        f.write(f"tipo_dado={tipo_dado}\n")
        f.write(f"num_tiradas={num_tiradas}\n")



def simular_tiradas(ruta: Path, tipo_dado: str, num_tiradas: int) -> None:
    # Como defino los dados como d4, d6, d10... me quito el primer caracter "d" y convierto el resto a entero para obtener el número de caras del dado, que es necesario para simular las tiradas
    caras = int(tipo_dado[1:])

    # Abro el fihero de simulación en modo escritura y escribo el resultado de cada tirada en una línea diferente.
    # En este caso se hace una escritura por cada tirada, otra opción sería generar todas las tiradas primero y luego escribirlas todas de golpe.
    # Qué caso usar depende de los requisitos del problema a resolver. Si el número de tiradas es muy grande, lo mejor sería escribir cada tirada a medida que se va generando para no tener que almacenar todas las tiradas en memoria, pero si el número de tiradas es pequeño, lo más sencillo es generar todas las tiradas primero y luego escribirlas todas de golpe.
    # En cualquier caso como no se especifica nada de cara al examen ambas versiones serían correctas. 
    with open(ruta, "w", encoding="utf-8") as f:
        for _ in range(num_tiradas):
            tirada = random.randint(1, caras)
            f.write(f"{tirada}\n")


if __name__ == "__main__":
    ruta_config = Path(__file__).parent / "config.txt"
    ruta_simulacion = Path(__file__).parent / "simulacion.txt"

    # Empezamos leyendo la configuración
    tipo_dado, num_tiradas = leer_config(ruta_config)

    while True:

        print("\n1. Simular")
        print("2. Configurar")
        print("0. Salir")
        opcion = int(input("Elige una opción: "))

        if opcion == 1:
            simular_tiradas(ruta_simulacion, tipo_dado, num_tiradas)
            print("Simulación realizada correctamente.")

        elif opcion == 2:
            print(f"Configuración actual: {tipo_dado}, {num_tiradas} tiradas")
            respuesta = input("¿Quieres cambiar la configuración? (S/N): ")

            if respuesta.lower() == "s":
                tipo_dado = input("Nuevo tipo de dado: ")
                num_tiradas = int(input("Nuevo número de tiradas: "))

                guardar_config(ruta_config, tipo_dado, num_tiradas)
                print("Configuración guardada correctamente.")
            else:
                print("Configuración no modificada.")

        elif opcion == 0:
            print("Saliendo del programa...")
            break

        else:
            print("Opción no válida.")