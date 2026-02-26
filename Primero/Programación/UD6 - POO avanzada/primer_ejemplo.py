class Miembro:
    def __init__(self, nombre: str, nss: str, correo: str):
        self.nombre = nombre
        self.nss = nss
        self.correo = correo

    def enviar_correo(self, mensaje: str) -> None:
        # Aquí se enviaría un correo al miembro usando self.correo
        pass


class Empleado(Miembro):
    def __init__(self, nombre: str, nss: str, correo: str, sueldo: float):
        super().__init__(nombre, nss, correo)
        self.sueldo = sueldo

    def generar_nomina(self) -> None:
        # Aquí se calcularía la nómina del empleado
        pass


class Practico(Miembro):
    def __init__(self, nombre: str, nss: str, correo: str, instituto_procedencia: str):
        super().__init__(nombre, nss, correo)
        self.instituto_procedencia = instituto_procedencia

    def evaluar(self) -> None:
        # Aquí se evaluaría el desempeño del práctico
        pass

if __name__ == "__main__":
    empleado = Empleado("Luis", "456", "luis@empresa.com", 1800.0)
    practico = Practico("Marta", "789", "marta@empresa.com", "IES Zaidín Vergeles")

    # --- Accesos correctos a atributos heredados ---
    print(empleado.nombre)   # heredado de Miembro
    print(practico.correo)   # heredado de Miembro

    # --- Accesos correctos a atributos propios ---
    print(empleado.sueldo)
    print(practico.instituto_procedencia)

    # --- Accesos erróneos (no existen en esa clase) ---
    # print(practico.sueldo)                  # Error: Practico no tiene sueldo
    # print(empleado.instituto_procedencia)   # Error: Empleado no tiene instituto

    # --- Métodos heredados ---
    empleado.enviar_correo("Reunión a las 10")
    practico.enviar_correo("Entrega del informe")

    # --- Métodos específicos ---
    empleado.generar_nomina()
    practico.evaluar()

    # --- Métodos erróneos ---
    # practico.generar_nomina()  # Error: Practico no genera nómina
    # empleado.evaluar()         # Error: Evaluar es propio del Practico