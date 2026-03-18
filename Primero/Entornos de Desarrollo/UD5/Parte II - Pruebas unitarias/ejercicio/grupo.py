from estudiante import Estudiante


class Grupo:

    def __init__(self, id: int, nombre: str):
        self.id = id
        self.nombre = nombre
        self.estudiantes: list[Estudiante] = []

    def agregar(self, estudiante: Estudiante):
        self.estudiantes.append(estudiante)

    def eliminar(self, id_estudiante: int):
        self.estudiantes = [
            e for e in self.estudiantes if e.id != id_estudiante
        ]

    def buscar_por_id(self, id_estudiante: int):
        for e in self.estudiantes:
            if e.id == id_estudiante:
                return e
        return None

    def promocionados(self) -> list[Estudiante]:
        return [e for e in self.estudiantes if e.promocionar()]

    def ordenar_por_media(self) -> list[Estudiante]:
        return sorted(self.estudiantes, key=lambda e: e.media())

    def media_grupo(self) -> float:
        if not self.estudiantes:
            return 0
        return sum(e.media() for e in self.estudiantes) / len(self.estudiantes)