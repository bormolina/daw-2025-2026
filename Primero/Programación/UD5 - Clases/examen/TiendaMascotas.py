from Mascota import Mascota

class TiendaMascotas:
    def __init__(self, id: int, nombre: str, direccion: str, mascotas: list[Mascota]):
        self.id = id
        self.nombre = nombre
        self.direccion = direccion
        self.disponibles = []
        self.vendidas = []

        for m in mascotas:
            if m.fecha_venta is None:
                self.disponibles.append(m)
            else:
                self.vendidas.append(m)

    def añadir_mascota(self, mascota: Mascota) -> None:
        if mascota.fecha_venta is None:
            self.disponibles.append(mascota)
        else:
            self.vendidas.append(mascota)

    def eliminar_mascota(self, id: int) -> bool:
        for lista in (self.disponibles, self.vendidas):
            for m in lista:
                if m.id == id:
                    lista.remove(m)
                    return True
        return False

    def mascotas_rango_precio(self, a: float, b: float) -> list[Mascota]:
        return [m for m in self.disponibles if a <= m.precio <= b]

    def no_necesitan_vacunas(self) -> list[Mascota]:
        return [m for m in self.disponibles if m.vacunas is None]

    def mas_antiguas(self) -> list[Mascota]:
        return sorted(self.disponibles, key=lambda m: m.fecha_entrada)

    def mascotas_por_tipo(self, tipo: str) -> list[Mascota]:
        return [m for m in self.disponibles if m.tipo == tipo]

    def mascotas_por_tipos(self, tipos: list[str]) -> list[Mascota]:
        return [m for m in self.disponibles if m.tipo in tipos]
    
    def actualizar_precio_por_tipo(self, tipo: str, porcentaje: float) -> None:
        factor = 1 + (porcentaje / 100)
        for m in self.disponibles:
            if m.tipo == tipo:
                m.precio *= factor

    def reporte_por_tipo(self) -> dict[str, dict[str, float]]:
        reporte = {}
        for m in self.vendidas:
            if m.tipo not in reporte:
                reporte[m.tipo] = {"num_vendidas": 0, "dinero": 0.0}
            reporte[m.tipo]["num_vendidas"] += 1
            reporte[m.tipo]["dinero"] += m.precio
        return reporte

if __name__ == "__main__":
    from datos import get_datos  # función que devuelve la lista de Mascota

    mascotas = get_datos()
    tienda = TiendaMascotas(1, "Animalia", "Calle Falsa 123", mascotas)

    print("=== DISPONIBLES ===")
    for m in tienda.disponibles:
        print(m)

    print("\n=== VENDIDAS ===")
    for m in tienda.vendidas:
        print(m)

    print("\n=== MASCOTAS EN RANGO DE PRECIO (100 - 200) ===")
    print([m.id for m in tienda.mascotas_rango_precio(100, 200)])

    print("\n=== NO NECESITAN VACUNAS ===")
    print([m.id for m in tienda.no_necesitan_vacunas()])

    print("\n=== MÁS ANTIGUAS (ordenadas por fecha de entrada) ===")
    print([m.id for m in tienda.mas_antiguas()])

    print("\n=== MASCOTAS POR TIPO 'Gato' ===")
    print([m.id for m in tienda.mascotas_por_tipo("Gato")])

    print("\n=== MASCOTAS POR TIPOS ['Gato', 'Erizo'] ===")
    print([m.id for m in tienda.mascotas_por_tipos(["Gato", "Erizo"])])

    print("\n=== ACTUALIZAR PRECIO +10% A LOS GATOS ===")
    tienda.actualizar_precio_por_tipo("Gato", 10)
    print([(m.id, m.precio) for m in tienda.mascotas_por_tipo("Gato")])

    print("\n=== REPORTE POR TIPO (VENDIDAS) ===")
    print(tienda.reporte_por_tipo())

    print("\n=== ELIMINAR MASCOTA ID 3 ===")
    print("Eliminada:", tienda.eliminar_mascota(3))
    print("IDs disponibles tras eliminar:", [m.id for m in tienda.disponibles])

    print("\n=== AÑADIR NUEVA MASCOTA ===")
    from datetime import datetime, timedelta
    nueva = Mascota(99, "Ghost", "Gato", datetime.today(), 180.0,
                    datetime.today() - timedelta(days=200), None, ["Rabia"])
    tienda.añadir_mascota(nueva)
    print("IDs disponibles tras añadir:", [m.id for m in tienda.disponibles])