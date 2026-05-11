from pathlib import Path
import sqlite3


RUTA_BD = Path(__file__).parent / "stock.db"


def conectar() -> sqlite3.Connection:
    return sqlite3.connect(RUTA_BD)


def crear_tabla(conexion: sqlite3.Connection) -> None:
    cursor = conexion.cursor()

    cursor.execute("""
        CREATE TABLE IF NOT EXISTS stock (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            producto TEXT NOT NULL UNIQUE,
            categoria TEXT NOT NULL,
            precio REAL NOT NULL CHECK (precio >= 0)
        )
    """)

    conexion.commit()


def insertar_datos(conexion: sqlite3.Connection) -> None:
    cursor = conexion.cursor()

    productos = [
        ("Teclado mecanico", "Informatica", 49.99),
        ("Raton inalambrico", "Informatica", 19.95),
        ("Monitor 24 pulgadas", "Informatica", 129.90),
        ("Disco SSD 1TB", "Informatica", 84.50),
        ("Memoria USB 64GB", "Informatica", 8.99),
        ("Silla de oficina", "Mobiliario", 89.99),
        ("Mesa escritorio", "Mobiliario", 149.00),
        ("Lampara LED", "Mobiliario", 22.50),
        ("Archivador metalico", "Mobiliario", 64.95),
        ("Caja herramientas", "Herramientas", 34.99),
        ("Taladro electrico", "Herramientas", 59.90),
        ("Destornillador precision", "Herramientas", 7.50),
        ("Martillo", "Herramientas", 11.95),
        ("Guantes trabajo", "Seguridad", 5.99),
        ("Gafas proteccion", "Seguridad", 6.50),
        ("Extintor pequeno", "Seguridad", 24.95),
        ("Cuaderno A4", "Papeleria", 2.75),
        ("Boligrafo azul", "Papeleria", 0.60),
        ("Paquete folios", "Papeleria", 4.80),
        ("Grapadora", "Papeleria", 6.99),
    ]

    # INSERT OR IGNORE inserta el producto si no existe; si ya existe, lo ignora.
    # Asi podemos ejecutar este script varias veces sin duplicar productos.
    cursor.executemany("""
        INSERT OR IGNORE INTO stock (producto, categoria, precio)
        VALUES (?, ?, ?)
    """, productos)

    conexion.commit()


def main() -> None:
    conexion = None

    try:
        conexion = conectar()
        crear_tabla(conexion)
        insertar_datos(conexion)
        print("stock.db creado correctamente.")
    except sqlite3.Error as error:
        print(f"Ha habido un error con la base de datos: {error}")
    finally:
        if conexion is not None:
            conexion.close()


if __name__ == "__main__":
    main()
