from pathlib import Path

nombre = input("¿Cómo te llamas? ")
edad = input("¿Cuántos años tienes? ")
ruta_fichero = Path(__file__).parent / "datos_ejemplo_escritura.txt"

with open(ruta_fichero, "a", encoding="utf-8") as f:
  f.write(f"Te llamas: {nombre} y tienes {edad} años\n")