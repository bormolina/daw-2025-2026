import random
from pathlib import Path


ruta_config = Path(__file__).parent / "ej4-config.txt"
ruta_salida = Path(__file__).parent / "ejercicio4-resultado.txt"


def es_primo(n: int, d: int = 2) -> bool:
    return False if n < 2 else True if d * d > n else False if n % d == 0 else es_primo(n, d + 1)

def leer_config() -> dict:
    config = {
        "inicio": "1",
        "fin": "100",
        "cantidad": "10",
        "salida": "pantalla",
        "solo_primos": "false"
    }

    # Si el fichero de configuración no existe, lo creamos con los valores por defecto y lo devolvemos
    if not ruta_config.exists():
        with open(ruta_config, "w", encoding="utf-8") as f:
            for clave, valor in config.items():
                f.write(f"{clave}:{valor}\n")
        return config

    with open(ruta_config, "r", encoding="utf-8") as f:
        for linea in f:
            if ":" in linea:
                clave, valor = linea.strip().split(":", 1)
                config[clave] = valor

    return config


def guardar_config(config: dict) -> None:
    with open(ruta_config, "w", encoding="utf-8") as f:
        for clave, valor in config.items():
            f.write(f"{clave}:{valor}\n")


def mostrar_config(config: dict) -> None:
    print("\n--- CONFIGURACIÓN ACTUAL ---")
    for clave, valor in config.items():
        print(f"{clave}: {valor}")


def generar_numeros(config: dict) -> list[int]:
    inicio = int(config["inicio"])
    fin = int(config["fin"])
    cantidad = int(config["cantidad"])
    solo_primos = config["solo_primos"].lower() == "true"

    numeros = []

    while len(numeros) < cantidad:
        n = random.randint(inicio, fin)

        if solo_primos:
            if es_primo(n):
                numeros.append(n)
        else:
            numeros.append(n)

    return numeros


def mostrar_resultados(numeros: list[int], config: dict) -> None:
    if config["salida"] == "fichero":
        with open(ruta_salida, "w", encoding="utf-8") as f:
            for num in numeros:
                f.write(f"{num}\n")
        print("Resultados guardados en fichero.")
    else:
        print("Resultados:")
        print(numeros)


def configurar(config: dict) -> dict:
    mostrar_config(config)

    opcion = input("\n¿Quieres modificar la configuración? (s/n): ").lower()

    if opcion != "s":
        print("Saliendo de configuración.")
        return config

    print("\n--- EDITAR CONFIGURACIÓN ---")

    config["inicio"] = input(f"Inicio ({config['inicio']}): ") or config["inicio"]
    config["fin"] = input(f"Fin ({config['fin']}): ") or config["fin"]
    config["cantidad"] = input(f"Cantidad ({config['cantidad']}): ") or config["cantidad"]
    config["salida"] = input(f"Salida [pantalla/fichero] ({config['salida']}): ") or config["salida"]
    config["solo_primos"] = input(f"Solo primos [true/false] ({config['solo_primos']}): ") or config["solo_primos"]

    guardar_config(config)
    print("Configuración guardada.")

    return config

    
if __name__ == "__main__":
    config = leer_config()

    while True:
        print("\n--- MENÚ ---")
        print("1. Calcular")
        print("2. Configurar")
        print("3. Salir")

        opcion = input("Elige opción: ")

        if opcion == "1":
            numeros = generar_numeros(config)
            mostrar_resultados(numeros, config)

        elif opcion == "2":
            config = configurar(config)

        elif opcion == "3":
            print("Saliendo...")
            break

        else:
            print("Opción no válida.")