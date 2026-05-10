from pathlib import Path
import sqlite3

RUTA_BD = Path(__file__).parent / "ejemplo1.db"

conexion = None

try:
    conexion = sqlite3.connect(RUTA_BD)
    print("Conexion realizada correctamente.")
except sqlite3.Error as error:
    print(f"Ha habido un error al conectar con la base de datos: {error}")
finally:
    if conexion is not None:
        conexion.close()
