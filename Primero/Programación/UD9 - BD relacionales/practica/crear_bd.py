from pathlib import Path
import sqlite3


RUTA_BD = Path(__file__).parent / "coleccion_vinilos.bd"


def conectar() -> sqlite3.Connection:
    conexion = sqlite3.connect(RUTA_BD)
    conexion.execute("PRAGMA foreign_keys = ON")
    return conexion


def crear_tablas(conexion: sqlite3.Connection) -> None:
    cursor = conexion.cursor()

    cursor.execute("""
        CREATE TABLE IF NOT EXISTS grupos (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            nombre TEXT NOT NULL UNIQUE
        )
    """)

    cursor.execute("""
        CREATE TABLE IF NOT EXISTS vinilos (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            nombre TEXT NOT NULL,
            id_grupo INTEGER NOT NULL,

            UNIQUE (nombre, id_grupo),
            FOREIGN KEY (id_grupo) REFERENCES grupos(id)
        )
    """)

    conexion.commit()


def insertar_datos(conexion: sqlite3.Connection) -> None:
    cursor = conexion.cursor()

    grupos = [
        ("The Cure",),
        ("Radiohead",),
        ("Nirvana",),
        ("Daft Punk",),
        ("Rosalia",),
    ]

    vinilos = [
        ("Disintegration", "The Cure"),
        ("OK Computer", "Radiohead"),
        ("In Rainbows", "Radiohead"),
        ("Nevermind", "Nirvana"),
        ("Random Access Memories", "Daft Punk"),
        ("El Mal Querer", "Rosalia"),
    ]

    cursor.executemany("""
        INSERT OR IGNORE INTO grupos (nombre)
        VALUES (?)
    """, grupos)

    for nombre_vinilo, nombre_grupo in vinilos:
        cursor.execute("""
            SELECT id
            FROM grupos
            WHERE nombre = ?
        """, (nombre_grupo,))

        id_grupo = cursor.fetchone()[0]

        cursor.execute("""
            INSERT OR IGNORE INTO vinilos (nombre, id_grupo)
            VALUES (?, ?)
        """, (nombre_vinilo, id_grupo))

    conexion.commit()


def mostrar_resumen(conexion: sqlite3.Connection) -> None:
    cursor = conexion.cursor()

    cursor.execute("SELECT COUNT(*) FROM grupos")
    total_grupos = cursor.fetchone()[0]

    cursor.execute("SELECT COUNT(*) FROM vinilos")
    total_vinilos = cursor.fetchone()[0]

    print("Base de datos creada correctamente.")
    print(f"Ruta: {RUTA_BD}")
    print(f"Grupos: {total_grupos}")
    print(f"Vinilos: {total_vinilos}")


def main() -> None:
    conexion = None

    try:
        conexion = conectar()
        crear_tablas(conexion)
        insertar_datos(conexion)
        mostrar_resumen(conexion)
    except sqlite3.Error as error:
        print(f"Ha habido un error con la base de datos: {error}")
    finally:
        if conexion is not None:
            conexion.close()


if __name__ == "__main__":
    main()
