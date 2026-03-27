import random
from pathlib import Path


def leer_config(ruta) -> dict[str, str | int | list[str]]:
    config = {}
    with open(ruta, "r", encoding="utf-8") as f:
        # Inserto las claves y valores
        for linea in f:
            clave, valor = linea.strip().split("=")
            config[clave] = valor

    # Convierto los valores a sus tipos correspondientes, no puedo hacerlo de forma general porque a priori no se saben los tipos de cada clave
    config["min"] = int(config["min"])
    config["max"] = int(config["max"])
    config["operaciones"] = config["operaciones"].split(",")
    config["n_vidas"] = int(config["n_vidas"])

    return config


def guardar_config(ruta, config: dict[str, str | int | list[str]]) -> None:
    with open(ruta, "w", encoding="utf-8") as f:
        f.write(f"min={config['min']}\n")
        f.write(f"max={config['max']}\n")
        f.write(f"operaciones={','.join(config['operaciones'])}\n")
        f.write(f"n_vidas={config['n_vidas']}\n")


def generar_cuenta(config: dict[str, str | int | list[str]]) -> tuple[int, int, str, int]:
    a = random.randint(config["min"], config["max"])
    b = random.randint(config["min"], config["max"])
    op = random.choice(config["operaciones"])

    if op == "+":
        resultado = a + b
    elif op == "-":
        resultado = a - b
    else:
        resultado = a * b

    return a, b, op, resultado


def jugar(config: dict[str, str | int | list[str]]) -> int:
    vidas = config["n_vidas"]
    puntos = 0
    print("\nComienza la partida")

    while vidas > 0:
        a, b, op, resultado = generar_cuenta(config)
        print(f"\n¿Cuánto es {a} {op} {b}?")
        try:
            respuesta = int(input("Respuesta: "))
        except:
            print("Debes introducir un número")
            continue # Volvemos al principio del bucle sin restar vidas ni nada, simplemente se vuelve a preguntar la misma cuenta

        if respuesta == resultado:
            print("Correcto")
            puntos += 1
        else:
            vidas -= 1
            print(f"Incorrecto. Te quedan {vidas} vidas")

    print(f"\nFin de la partida. Puntuación: {puntos}")

    return puntos


def guardar_record(ruta: Path, puntos: int) -> None:
    records = []

    if ruta.exists(): #comprobamos si el archivo existe para no intentar leerlo si no existe, lo que daría error
        with open(ruta, "r", encoding="utf-8") as f:
            for linea in f:
                records.append(int(linea.strip()))

    records.append(puntos)

    records.sort(reverse=True)
    records = records[:5]

    with open(ruta, "w", encoding="utf-8") as f:
        for r in records:
            f.write(str(r) + "\n")


def ver_ranking(ruta: Path) -> None:
    if not ruta.exists():
        print("\nNo hay puntuaciones todavía")
        return

    print("\n--- RANKING ---")
    with open(ruta, "r", encoding="utf-8") as f:
        for i, linea in enumerate(f, 1):
            print(f"{i}. {linea.strip()}")


def configurar(config: dict[str, str | int | list[str]], ruta: Path) -> None:

    print("\nConfiguración actual:")
    print(config)

    config["min"] = int(input("Nuevo mínimo: "))
    config["max"] = int(input("Nuevo máximo: "))

    ops = input("Operaciones permitidas (+,-,* separadas por coma): ")
    config["operaciones"] = ops.split(",")

    config["n_vidas"] = int(input("Número de vidas: "))

    guardar_config(ruta, config)

    print("Configuración guardada")


if __name__ == "__main__":
    carpeta = Path(__file__).parent
    ruta_config = carpeta / "config.txt"
    ruta_records = carpeta / "records.txt"
    config = leer_config(ruta_config)

    while True:
        print("\n--- MENÚ ---")
        print("1. Jugar")
        print("2. Configuración")
        print("3. Ver ranking")
        print("4. Salir")

        opcion = input("Elige una opción: ")

        if opcion == "1":
            puntos = jugar(config)
            guardar_record(ruta_records, puntos)

        elif opcion == "2":
            configurar(config, ruta_config)

        elif opcion == "3":
            ver_ranking(ruta_records)

        elif opcion == "4":
            print("Hasta luego")
            break

        else:
            print("Opción no válida")