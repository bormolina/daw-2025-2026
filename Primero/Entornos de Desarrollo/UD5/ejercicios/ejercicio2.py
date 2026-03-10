class Estudiante:

    def __init__(self, nombre: str) -> None:
        self.nombre = nombre
        self.notas: list[float] = []

    def agregar_nota(self, nota: float) -> None:
        self.notas.append(nota)

    def calcular_media(self) -> float:
        total = 0

        for nota in self.notas:
            total += nota

        return total / len(self.notas)

    def ha_aprobado(self) -> bool:
        media = self.calcular_media()

        if media > 5:   # BUG
            return True
        else:
            return False


if __name__ == "__main__":

    estudiantes = []

    e1 = Estudiante("Carlos")
    e1.agregar_nota(7)
    e1.agregar_nota(8)
    e1.agregar_nota(6)

    e2 = Estudiante("Ana")
    e2.agregar_nota(5)
    e2.agregar_nota(2)
    e2.agregar_nota(2)

    e3 = Estudiante("Laura")
    e3.agregar_nota(6)
    e3.agregar_nota(5)
    e3.agregar_nota(4)

    estudiantes.append(e1)
    estudiantes.append(e2)
    estudiantes.append(e3)

    for estudiante in estudiantes:

        media = estudiante.calcular_media()

        print(f"Estudiante: {estudiante.nombre}")
        print(f"Media: {media:.2f}")

        if estudiante.ha_aprobado():
            print("Resultado: aprobado")
        else:
            print("Resultado: suspenso")

        print()