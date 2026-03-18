from personaje import Personaje

class Equipo:
    def __init__(self):
        self.personajes: list[Personaje] = []

    def agregar(self, personaje: Personaje):
        self.personajes.append(personaje)

    def eliminar(self, nombre: str):
        self.personajes = [p for p in self.personajes if p.nombre != nombre]

    def buscar_por_clase(self, clase: str) -> list[Personaje]:
        return [p for p in self.personajes if p.clase == clase]

    def ordenar_por_nivel(self) -> list[Personaje]:
        return sorted(self.personajes, key=lambda p: p.nivel)

    def media_nivel(self) -> float:
        if not self.personajes:
            return 0
        return sum(p.nivel for p in self.personajes) / len(self.personajes)