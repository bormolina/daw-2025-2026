from datetime import datetime

class Pedido:
    def __init__(
        self,
        id_pedido: int, # Identificador único del pedido
        tipo: str,  # tipo de leña: "roble", "pino", "abedul", ...
        peso_kg: float,
        direccion: list,          # [calle, numero, localidad]
        fecha_pedido: datetime,
        fecha_entrega: datetime,
        precio: float,
        transportista: str
    ):
        self.id_pedido = id_pedido
        self.tipo = tipo
        self.peso_kg = peso_kg
        self.direccion = direccion
        self.fecha_pedido = fecha_pedido
        self.fecha_entrega = fecha_entrega
        self.precio = precio
        self.transportista = transportista

    def precio_por_kg(self) -> float:
        return self.precio / self.peso_kg

    def __str__(self) -> str:
        return (
            f"Pedido #{self.id_pedido}\n"
            f"Tipo de leña: {self.tipo}\n"
            f"Peso (kg): {self.peso_kg}\n"
            f"Dirección: {self.direccion[0]} {self.direccion[1]}, {self.direccion[2]}\n"
            f"Fecha del pedido: {self.fecha_pedido}\n"
            f"Fecha de entrega: {self.fecha_entrega}\n"
            f"Precio total: {self.precio} €\n"
            f"Transportista: {self.transportista}"
        )