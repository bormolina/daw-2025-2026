from pathlib import Path
import sqlite3


RUTA_BD = Path(__file__).parent / "games.db"

# Creamos clases para Usuario y Videojuego porque son los datos que queremos manejar y mostrar.
# No creamos una clase para la relacion usuarios_juegos porque aqui solo la usamos para consultar.
# En programacion no todo es blanco o negro: depende del problema y de cuanta complejidad aporte cada clase.

class Usuario:
    def __init__(self, usuario_id: int, nombre_usuario: str) -> None:
        self.id = usuario_id
        self.nombre_usuario = nombre_usuario

    def __str__(self) -> str:
        return f"{self.id} - {self.nombre_usuario}"


class Videojuego:
    def __init__(self, titulo: str, genero: str, horas_jugadas: float, favorito: int) -> None:
        self.titulo = titulo
        self.genero = genero
        self.horas_jugadas = horas_jugadas
        self.favorito = bool(favorito)

    def __str__(self) -> str:
        texto_favorito = "si" if self.favorito else "no"
        return f"{self.titulo} ({self.genero}) - {self.horas_jugadas} horas - favorito: {texto_favorito}"


def conectar() -> sqlite3.Connection:
    conexion = sqlite3.connect(RUTA_BD)
    # Activamos las claves ajenas en esta conexion de SQLite.
    conexion.execute("PRAGMA foreign_keys = ON")
    return conexion


def obtener_usuarios(conexion: sqlite3.Connection) -> list[Usuario]:
    # Creamos un cursor para poder ejecutar consultas SQL.
    cursor = conexion.cursor()

    # execute() lanza una sentencia SQL contra la base de datos.
    cursor.execute("""
        SELECT id, nombre_usuario
        FROM usuarios
        ORDER BY id
    """)

    # fetchall() recoge todas las filas devueltas por el SELECT. Devuelve una lista de tuplas, donde cada tupla representa una fila de la tabla y tendra tantos elementos como columnas en la consulta, en este caso (id, nombre_usuario).
    filas = cursor.fetchall()

    usuarios = []

    for usuario_id, nombre_usuario in filas:
        usuarios.append(Usuario(usuario_id, nombre_usuario))

    return usuarios


def mostrar_usuarios(conexion: sqlite3.Connection) -> None:
    usuarios = obtener_usuarios(conexion)

    print("\nUsuarios")
    print("--------")

    for usuario in usuarios:
        print(usuario)

    print("0 - Salir")


def obtener_juegos_usuario(conexion: sqlite3.Connection, usuario_id: int) -> list[Videojuego]:
    cursor = conexion.cursor()

    # Lo estamos haciendo bien: el dato del usuario se pasa con ?, no pegandolo al SQL.
    # La coma final en (usuario_id,) es necesaria para crear una tupla de un solo elemento.
    cursor.execute("""
        SELECT juegos.titulo,
               juegos.genero,
               usuarios_juegos.horas_jugadas,
               usuarios_juegos.favorito
        FROM usuarios_juegos
        JOIN juegos ON usuarios_juegos.juego_id = juegos.id
        WHERE usuarios_juegos.usuario_id = ?
        ORDER BY juegos.titulo
    """, (usuario_id,))

    filas = cursor.fetchall()

    videojuegos = []

    for titulo, genero, horas_jugadas, favorito in filas:
        videojuegos.append(Videojuego(titulo, genero, horas_jugadas, favorito))

    return videojuegos


def mostrar_juegos_usuario(conexion: sqlite3.Connection, usuario_id: int) -> None:
    juegos = obtener_juegos_usuario(conexion, usuario_id)

    if not juegos:
        print("Ese usuario no existe o no tiene juegos.")
        return

    print("\nJuegos del usuario")
    print("------------------")

    for juego in juegos:
        print(juego)


def main() -> None:
    conexion = None

    try:
        conexion = conectar()
    # Capturamos sqlite3.Error porque es mas especifico que capturar cualquier Exception.
    except sqlite3.Error as error:
        print(f"Ha habido un error al conectar con la base de datos: {error}")
        return
    # El try es pequeñito: solo comprobamos la conexion y no metemos todo el programa dentro.
    
    while True:
        mostrar_usuarios(conexion)
        opcion = input("\nIntroduce el id de un usuario: ").strip()

        if opcion == "0":
            print("Programa terminado.")
            break

        if not opcion.isdigit():
            print("Debes introducir un numero de usuario o 0 para salir.")
            continue

        mostrar_juegos_usuario(conexion, int(opcion))

    if conexion is not None:
        conexion.close()


if __name__ == "__main__":
    main()
