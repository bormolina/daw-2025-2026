from datetime import datetime
from Producto import Producto


def productos_caros(productos: list[Producto], precio_min: float) -> list[Producto]:
    return [p for p in productos if p.precio >= precio_min]


def productos_de_categoria(productos: list[Producto], categoria: str) -> list[Producto]:
    return [p for p in productos if categoria in p.categorias]


def productos_multicategoria(productos: list[Producto]) -> list[Producto]:
    return [p for p in productos if len(p.categorias) > 1]


def productos_caducados(productos: list[Producto]) -> list[Producto]:
    hoy = datetime.today()
    return [p for p in productos if p.fecha_caducidad < hoy]


def producto_mas_caro(productos: list[Producto]) -> Producto | None:
    if len(productos) == 0:
        return None
    return max(productos, key=lambda p: p.precio)


def ordenar_por_caducidad(productos: list[Producto]) -> list[Producto]:
    return sorted(productos, key=lambda p: p.fecha_caducidad)


def hay_productos_caducados(productos: list[Producto]) -> bool:
    hoy = datetime.today()
    for p in productos:
        if p.fecha_caducidad < hoy:
            return True
    return False


def eliminar_caducados(productos: list[Producto]) -> list[Producto]:
    hoy = datetime.today()
    return [p for p in productos if p.fecha_caducidad >= hoy]


def dias_en_super(productos: list[Producto]) -> dict[int, int]:
    hoy = datetime.today()
    return {p.id: (hoy - p.fecha_entrada).days for p in productos}


def conteo_por_categoria(productos: list[Producto]) -> dict[str, int]:
    conteo = {}
    for p in productos:
        for cat in p.categorias:
            conteo[cat] = conteo.get(cat, 0) + 1
    return conteo

if __name__ == "__main__":
    from datos import get_productos

    productos = get_productos()

    print("=== PRODUCTOS CAROS (>= 2.0€) ===")
    print([p.id for p in productos_caros(productos, 2.0)])

    print("\n=== PRODUCTOS DE CATEGORÍA 'Lácteos' ===")
    print([p.id for p in productos_de_categoria(productos, "Lácteos")])

    print("\n=== PRODUCTOS MULTICATEGORÍA ===")
    print([p.id for p in productos_multicategoria(productos)])

    print("\n=== PRODUCTOS CADUCADOS ===")
    print([p.id for p in productos_caducados(productos)])

    print("\n=== PRODUCTO MÁS CARO ===")
    p_caro = producto_mas_caro(productos)
    print(p_caro.id if p_caro else None)

    print("\n=== ORDENADOS POR CADUCIDAD ===")
    print([p.id for p in ordenar_por_caducidad(productos)])

    print("\n=== ¿HAY PRODUCTOS CADUCADOS? ===")
    print(hay_productos_caducados(productos))

    print("\n=== ELIMINAR CADUCADOS ===")
    print([p.id for p in eliminar_caducados(productos)])

    print("\n=== DÍAS EN EL SUPERMERCADO ===")
    print(dias_en_super(productos))

    print("\n=== CONTEO POR CATEGORÍA ===")
    print(conteo_por_categoria(productos))