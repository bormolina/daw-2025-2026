juegos_javier = ["Dark Souls", "Hollow Knight", "Celeste", "Celeste", "Elden Ring", "Hades"]
juegos_marta  = ["Hollow Knight", "Stardew Valley", "Hades", "Hades", "Terraria"]


# Convertimos las listas en conjuntos (elimina repetidos automáticamente)
set_javier = set(juegos_javier)
set_marta = set(juegos_marta)


# Realizamos cálculos
print("a) Juegos que tienen ambos:", ambos = list(set_javier & set_marta))
print("b) Juegos que tiene Javier pero no Marta:", list(set_javier - set_marta))
print("c) Juegos que tiene Marta pero no Javier:", list(set_marta - set_javier))
print("c) ¿Javier tiene repetidos?", len(juegos_javier) != len(set_javier))
print("d) ¿Marta tiene repetidos?", repetidos_marta = len(juegos_marta) != len(set_marta))
print("d) Biblioteca conjunta:", list(set_javier | set_marta))