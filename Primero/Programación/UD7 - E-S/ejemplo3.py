# Leer un fichero de texto todas las líneas a la vez y contar cuántas líneas empiezan por la letra a

with open("quijote.txt", "r", encoding="utf-8") as f:
    lineas = f.readlines()
    contador = len([linea for linea in lineas if linea[0].lower() == "a"])


print(f"El Quijote tiene {contador} líneas que empiezan por a")