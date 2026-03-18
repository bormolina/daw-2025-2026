class Estudiante:

    def __init__(self, id: int, nombre: str, notas: list[float]):
        self.id = id
        self.nombre = nombre
        self.notas = notas

    def promocionar(self) -> bool:
        return all(n >= 5 for n in self.notas)

    def media(self) -> float:
        if not self.notas:
            return 0
        return sum(self.notas) / len(self.notas)

    def anadir_nota(self, nota: float):
        self.notas.append(nota)

    def __eq__(self, other):
        if not isinstance(other, Estudiante):
            return False
        return self.id == other.id