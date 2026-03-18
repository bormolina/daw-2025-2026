# Leer un fichero de texto línea a línea y contar cuántas líneas empiezan por la letra a

contador_lineas = 0
contador_a = 0

with open("quijote.txt", "r", encoding="utf-8") as f:
    for linea in f:
        contador_lineas += 1
        if linea[0].lower() == "a":
            contador_a += 1


print(f"El Quijote tiene un total de {contador_lineas} líneas de las cuales {contador_a} líneas que empiezan por a que representan un {contador_lineas/contador_a} del total")