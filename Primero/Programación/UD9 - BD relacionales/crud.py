from pathlib import Path
import sqlite3


RUTA_BD = Path(__file__).parent / "stock.db"


class Item:
    def __init__(self, item_id: int, producto: str, categoria: str | None = None, precio: float | None = None) -> None:
        self.id = item_id
        self.producto = producto
        self.categoria = categoria
        self.precio = precio

    def __str__(self) -> str:
        if self.categoria is None or self.precio is None:
            return f"{self.id} - {self.producto}"

        return f"{self.id} - {self.producto} ({self.categoria}) - {self.precio} euros"


def conectar() -> sqlite3.Connection:
    return sqlite3.connect(RUTA_BD)


def obtener_productos(conexion: sqlite3.Connection) -> list[Item]:
    cursor = conexion.cursor()

    cursor.execute("""
        SELECT id, producto
        FROM stock
        ORDER BY id
    """)

    filas = cursor.fetchall()

    productos = []

    for producto_id, producto in filas:
        productos.append(Item(producto_id, producto))

    return productos


def mostrar_productos(conexion: sqlite3.Connection) -> None:
    productos = obtener_productos(conexion)

    print("\nStock")
    print("-----")

    for producto in productos:
        print(producto)

    print("\nEscribe un id para consultar/modificar.")
    print("Escribe -id para borrar. Ejemplo: -3")
    print("[C]rear producto")
    print("[S]alir")


def pedir_precio(mensaje: str) -> float:
    while True:
        texto = input(mensaje).strip().replace(",", ".")

        try:
            precio = float(texto)
        except ValueError:
            print("El precio debe ser un numero.")
            continue

        if precio < 0:
            print("El precio no puede ser negativo.")
            continue

        return precio


def crear_producto(conexion: sqlite3.Connection) -> None:
    producto = input("Producto: ").strip()
    categoria = input("Categoria: ").strip()
    precio = pedir_precio("Precio: ")

    if producto == "" or categoria == "":
        print("El producto y la categoria son obligatorios.")
        return

    cursor = conexion.cursor()

    try:
        cursor.execute("""
            INSERT INTO stock (producto, categoria, precio)
            VALUES (?, ?, ?)
        """, (producto, categoria, precio))
        conexion.commit()
        print("Producto creado correctamente.")
    except sqlite3.IntegrityError as error:
        print(f"No se ha podido crear el producto: {error}")


def obtener_producto(conexion: sqlite3.Connection, producto_id: int) -> Item | None:
    cursor = conexion.cursor()

    cursor.execute("""
        SELECT id, producto, categoria, precio
        FROM stock
        WHERE id = ?
    """, (producto_id,))

    fila = cursor.fetchoneItem()

    if fila is None:
        return None

    producto_id, producto, categoria, precio = fila
    return Item(producto_id, producto, categoria, precio)


def consultar_producto(conexion: sqlite3.Connection, producto_id: int) -> None:
    producto = obtener_producto(conexion, producto_id)

    if producto is None:
        print("No existe ningun producto con ese id.")
        return

    print("\nProducto encontrado")
    print("-------------------")
    print(f"Id: {producto.id}")
    print(f"Producto: {producto.producto}")
    print(f"Categoria: {producto.categoria}")
    print(f"Precio: {producto.precio}")

    respuesta = input("Quieres modificar algun parametro? [S/N]: ").strip().lower()

    if respuesta != "s":
        return

    nuevo_nombre = input(f"Nuevo producto [{producto.producto}]: ").strip()
    nueva_categoria = input(f"Nueva categoria [{producto.categoria}]: ").strip()
    nuevo_precio_texto = input(f"Nuevo precio [{producto.precio}]: ").strip()

    if nuevo_nombre == "":
        nuevo_nombre = producto.producto

    if nueva_categoria == "":
        nueva_categoria = producto.categoria

    if nuevo_precio_texto == "":
        nuevo_precio = producto.precio
    else:
        try:
            nuevo_precio = float(nuevo_precio_texto.replace(",", "."))
        except ValueError:
            print("El precio debe ser un numero. No se ha modificado el producto.")
            return

        if nuevo_precio < 0:
            print("El precio no puede ser negativo. No se ha modificado el producto.")
            return

    cursor = conexion.cursor()

    try:
        cursor.execute("""
            UPDATE stock
            SET producto = ?,
                categoria = ?,
                precio = ?
            WHERE id = ?
        """, (nuevo_nombre, nueva_categoria, nuevo_precio, producto.id))
        conexion.commit()
        print("Producto modificado correctamente.")
    except sqlite3.IntegrityError as error:
        print(f"No se ha podido modificar el producto: {error}")


def borrar_producto(conexion: sqlite3.Connection, producto_id: int) -> None:
    cursor = conexion.cursor()

    cursor.execute("""
        DELETE FROM stock
        WHERE id = ?
    """, (producto_id,))

    conexion.commit()

    if cursor.rowcount == 0:
        print("No existe ningun producto con ese id.")
    else:
        print("Producto borrado correctamente.")


def procesar_opcion(conexion: sqlite3.Connection, opcion: str) -> bool:
    if opcion.lower() == "c":
        crear_producto(conexion)
    elif opcion.lower() == "s":
        return False
    elif opcion.startswith("-") and opcion[1:].isdigit():
        borrar_producto(conexion, int(opcion[1:]))
    elif opcion.isdigit():
        consultar_producto(conexion, int(opcion))
    else:
        print("Opcion no valida.")

    return True


def main() -> None:
    conexion = None

    try:
        conexion = conectar()
    except sqlite3.Error as error:
        print(f"No se ha podido conectar con la base de datos: {error}")
        return

    while True:
        mostrar_productos(conexion)
        opcion = input("\nOpcion: ").strip()

        if not procesar_opcion(conexion, opcion):
            print("Programa terminado.")
            break

    if conexion is not None:
        conexion.close()


if __name__ == "__main__":
    main()
