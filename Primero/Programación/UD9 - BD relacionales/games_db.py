from pathlib import Path
import sqlite3


RUTA_BD = Path(__file__).parent / "games.db"


def conectar() -> sqlite3.Connection:
    conexion = sqlite3.connect(RUTA_BD)
    # execute() sirve para ejecutar una sentencia SQL.
    conexion.execute("PRAGMA foreign_keys = ON")
    return conexion


def crear_tablas(conexion: sqlite3.Connection) -> None:
    # cursor() crea un cursor, que es el objeto que usamos para lanzar consultas SQL.
    cursor = conexion.cursor()

    cursor.execute("""
        CREATE TABLE IF NOT EXISTS usuarios (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            nombre_usuario TEXT NOT NULL UNIQUE,
            email TEXT NOT NULL UNIQUE,
            fecha_registro TEXT NOT NULL
        )
    """)

    cursor.execute("""
        CREATE TABLE IF NOT EXISTS juegos (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            titulo TEXT NOT NULL UNIQUE,
            genero TEXT NOT NULL,
            precio REAL NOT NULL CHECK (precio >= 0),
            fecha_lanzamiento TEXT
        )
    """)

    cursor.execute("""
        CREATE TABLE IF NOT EXISTS usuarios_juegos (
            usuario_id INTEGER NOT NULL,
            juego_id INTEGER NOT NULL,
            fecha_compra TEXT NOT NULL,
            horas_jugadas REAL NOT NULL DEFAULT 0 CHECK (horas_jugadas >= 0),
            favorito INTEGER NOT NULL DEFAULT 0 CHECK (favorito IN (0, 1)),

            PRIMARY KEY (usuario_id, juego_id),
            FOREIGN KEY (usuario_id) REFERENCES usuarios(id) ON DELETE CASCADE,
            FOREIGN KEY (juego_id) REFERENCES juegos(id) ON DELETE CASCADE
        )
    """)

    # commit() confirma los cambios para que queden guardados en la base de datos.
    conexion.commit()


def insertar_datos(conexion: sqlite3.Connection) -> None:
    cursor = conexion.cursor()

    usuarios = [
        ("maria99", "maria99@example.com", "2026-05-01"),
        ("alex_dev", "alex.dev@example.com", "2026-05-03"),
        ("samuel_22", "samuel22@example.com", "2026-05-06"),
    ]

    juegos = [
        ("Stardew Valley", "Simulacion", 13.99, "2016-02-26"),
        ("Hollow Knight", "Metroidvania", 14.99, "2017-02-24"),
        ("Portal 2", "Puzles", 9.75, "2011-04-19"),
        ("Celeste", "Plataformas", 19.50, "2018-01-25"),
    ]

    # executemany() ejecuta la misma sentencia SQL varias veces con distintos datos.
    cursor.executemany("""
        INSERT OR IGNORE INTO usuarios (nombre_usuario, email, fecha_registro)
        VALUES (?, ?, ?)
    """, usuarios)

    cursor.executemany("""
        INSERT OR IGNORE INTO juegos (titulo, genero, precio, fecha_lanzamiento)
        VALUES (?, ?, ?, ?)
    """, juegos)

    compras = [
        ("maria99", "Stardew Valley", "2026-05-02", 12.5, 1),
        ("maria99", "Portal 2", "2026-05-04", 3.0, 0),
        ("alex_dev", "Hollow Knight", "2026-05-04", 28.0, 1),
        ("alex_dev", "Celeste", "2026-05-05", 7.5, 0),
        ("samuel_22", "Portal 2", "2026-05-07", 1.5, 1),
    ]

    for nombre_usuario, titulo, fecha_compra, horas_jugadas, favorito in compras:
        cursor.execute(
            "SELECT id FROM usuarios WHERE nombre_usuario = ?",
            (nombre_usuario,),
        )
        # fetchone() recoge una sola fila del resultado de una consulta SELECT.
        usuario_id = cursor.fetchone()[0]

        cursor.execute(
            "SELECT id FROM juegos WHERE titulo = ?",
            (titulo,),
        )
        juego_id = cursor.fetchone()[0]

        cursor.execute("""
            INSERT OR IGNORE INTO usuarios_juegos
                (usuario_id, juego_id, fecha_compra, horas_jugadas, favorito)
            VALUES (?, ?, ?, ?, ?)
        """, (usuario_id, juego_id, fecha_compra, horas_jugadas, favorito))

    conexion.commit()


def mostrar_resumen(conexion: sqlite3.Connection) -> None:
    cursor = conexion.cursor()

    cursor.execute("SELECT COUNT(*) FROM usuarios")
    total_usuarios = cursor.fetchone()[0]

    cursor.execute("SELECT COUNT(*) FROM juegos")
    total_juegos = cursor.fetchone()[0]

    cursor.execute("SELECT COUNT(*) FROM usuarios_juegos")
    total_compras = cursor.fetchone()[0]

    print("Base de datos creada correctamente.")
    print(f"Ruta: {RUTA_BD}")
    print(f"Usuarios: {total_usuarios}")
    print(f"Juegos: {total_juegos}")
    print(f"Relaciones usuarios-juegos: {total_compras}")


def main() -> None:
    try:
        conexion = conectar()
        crear_tablas(conexion)
        insertar_datos(conexion)
        mostrar_resumen(conexion)
    except sqlite3.Error as error:
        print(f"Ha habido un error con la base de datos: {error}")
    finally:
        if "conexion" in locals():
            conexion.close()


if __name__ == "__main__":
    main()
