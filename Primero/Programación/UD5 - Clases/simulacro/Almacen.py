from datetime import date
from Mantecado import Mantecado


class Almacen:
    def __init__(self, id: int, direccion: str,
                 mantecados: list[Mantecado] | None = None):
        self.id = id
        self.direccion = direccion
        self.mantecados = mantecados if mantecados is not None else []

    # Número total de mantecados
    def total_mantecados(self) -> int:
        return len(self.mantecados)

    # Añadir mantecado
    def anadir_mantecado(self, mantecado: Mantecado) -> None:
        self.mantecados.append(mantecado)

    # Eliminar mantecado por id
    def eliminar_mantecado(self, id_mantecado: int) -> bool:
        for m in self.mantecados:
            if m.id == id_mantecado:
                self.mantecados.remove(m)
                return True
        return False

    # Mantecados ya caducados
    def mantecados_caducados(self) -> list[Mantecado]:
        hoy = date.today()
        return [m for m in self.mantecados
                if m.fecha_caducidad < hoy]

    # Mantecados a los que les faltan n o menos días para caducar
    def proximos_a_caducar(self, n: int) -> list[Mantecado]:
        hoy = date.today()
        return [m for m in self.mantecados
                if 0 <= (m.fecha_caducidad - hoy).days <= n]

    # Mantecados en un rango de precio
    def mantecados_en_rango_precio(self, minimo: float,
                                   maximo: float) -> list[Mantecado]:
        return [m for m in self.mantecados
                if minimo <= m.precio <= maximo]

    # Dado un ingrediente, los que NO lo tengan
    def sin_ingrediente(self, ingrediente: str) -> list[Mantecado]:
        return [m for m in self.mantecados
                if ingrediente not in m.ingredientes]

    # Reporte por ingrediente
    # {ingrediente: número de mantecados que lo contienen}
    def reporte_por_ingrediente(self) -> dict[str, int]:
        reporte = {}
        for m in self.mantecados:
            for ing in m.ingredientes:
                reporte[ing] = reporte.get(ing, 0) + 1
        return reporte

    # Reporte por tipo
    # {tipo: número de mantecados}
    def reporte_por_tipo(self) -> dict[str, int]:
        reporte = {}
        for m in self.mantecados:
            reporte[m.tipo] = reporte.get(m.tipo, 0) + 1
        return reporte
    
if __name__ == "__main__":
    from datos import get_mantecados
    from datetime import date, timedelta

    # Obtener lista base
    lista = get_mantecados(1)

    # Crear almacén con dirección más realista
    almacen = Almacen(
        1,
        "Avenida de Andalucía 45, 18014 Granada",
        lista
    )

    print("===== ESTADO INICIAL =====")
    print("Total mantecados:", almacen.total_mantecados())
    print()

    # Eliminar por id
    print("Eliminando mantecado con id 3...")
    print("Eliminado:", almacen.eliminar_mantecado(3))
    print("Total tras eliminar:", almacen.total_mantecados())
    print()

    # Añadir nuevo mantecado (recordando las DOS fechas)
    print("Añadiendo nuevo mantecado...")

    hoy = date.today()

    nuevo = Mantecado(
        99,
        "especial_navidad",
        hoy,                         
        hoy + timedelta(days=20),  
        4.0,
        ["harina", "manteca", "miel"]
    )

    almacen.anadir_mantecado(nuevo)

    print("Total tras añadir:", almacen.total_mantecados())
    print()

    # Caducados
    print("===== CADUCADOS =====")
    for m in almacen.mantecados_caducados():
        print(m.id, m.tipo)
    print()

    # Próximos a caducar
    print("===== PRÓXIMOS A CADUCAR (≤ 3 días) =====")
    for m in almacen.proximos_a_caducar(3):
        print(m.id, m.tipo)
    print()

    # Rango de precio
    print("===== RANGO DE PRECIO (2.0 - 3.0) =====")
    for m in almacen.mantecados_en_rango_precio(2.0, 3.0):
        print(m.id, m.tipo, m.precio)
    print()

    # Sin ingrediente
    print("===== SIN AZUCAR =====")
    for m in almacen.sin_ingrediente("azucar"):
        print(m.id, m.tipo)
    print()

    # Reporte por ingrediente
    print("===== REPORTE POR INGREDIENTE =====")
    for ing, cantidad in almacen.reporte_por_ingrediente().items():
        print(ing, "->", cantidad)
    print()

    # Reporte por tipo
    print("===== REPORTE POR TIPO =====")
    for tipo, cantidad in almacen.reporte_por_tipo().items():
        print(tipo, "->", cantidad)
