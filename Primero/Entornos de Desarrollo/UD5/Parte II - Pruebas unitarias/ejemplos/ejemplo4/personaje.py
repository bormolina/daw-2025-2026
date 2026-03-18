class Personaje:
    def __init__(self, nombre: str, clase: str, nivel: int, ataque: int, vida: int):
        self.nombre = nombre
        self.clase = clase
        self.nivel = nivel
        self.ataque = ataque
        self.vida = vida

    def subir_nivel(self):
        self.nivel += 1
        self.ataque += 2
        self.vida += 5

    def esta_vivo(self) -> bool:
        return self.vida > 0

    def recibir_dano(self, cantidad: int):
        self.vida -= cantidad