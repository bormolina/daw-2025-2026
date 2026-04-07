import json
from pathlib import Path


if __name__ == "__main__":
    ruta = Path(__file__).parent / "datos" / "lol.json"

    with open(ruta, "r", encoding="utf-8") as f:
        datos = json.load(f) # Recuerda que load devuelve un diccionario o una lista, dependiendo de lo que haya en el fichero JSON. En este caso, como el JSON es una lista de objetos (campeones), load nos devuelve una lista de diccionarios (cada diccionario representa un campeón con sus datos)

    print("Campeones recomendados para el profe:")

    for campeon in datos: # Cada campeon es un diccionario con claves "nombre", "posiciones" y "dificultad"
        nombre = campeon["nombre"]
        posiciones = campeon["posiciones"]
        dificultad = campeon["dificultad"]

    #Fíjate que cada campeon puede tener varias posiciones por lo tanto usamos "Top" in posiciones y no posiciones == "Top" pero como solo tiene una dificultad, ahí sí hacemos dificultad == "Baja"
        if "Top" in posiciones and dificultad == "Baja":
            print(nombre)