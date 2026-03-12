# Leer un fichero de texto línea a línea y contar cuántas líneas empiezan por la letra a

contador = 0

with open("quijote.txt", "r", encoding="utf-8") as f:
    for linea in f:
        if linea[0].lower() == "a":
            contador += 1


print(f"El Quijote tiene {contador} líneas que empiezan por a")