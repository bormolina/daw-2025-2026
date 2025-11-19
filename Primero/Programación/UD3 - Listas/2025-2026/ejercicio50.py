matriz = [
    ["Perro", "Gato", "Hámster"],
    ["Loro", "Conejo", "Tortuga"],
    ["Pez", "Hurón", "Ardilla"],
    ["Iguana", "Serpiente", "Erizo"]
]

num_animales = 0

for fila in matriz:
    for animal in fila:
        if animal[0].lower() in ["a", "e", "i", "o", "u"]:
            num_animales += 1

print(f"La cantidad de animales que empizan por vocal es: {num_animales}")