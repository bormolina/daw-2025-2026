from datetime import datetime
from pathlib import Path

class Venta:
    def __init__(self, id: int, producto: str, fecha: datetime, precio: float) -> None:
        self.id = id
        self.producto = producto
        self.fecha = fecha
        self.precio = precio

    def __str__(self) -> str:
        fecha_str = self.fecha.strftime("%d/%m/%Y")
        return f"{self.id} - {self.producto} - {fecha_str} - {self.precio:.2f}€"


def es_enero_2022(fecha: datetime) -> bool:
    return fecha.month == 1 and fecha.year == 2022


if __name__ == "__main__":
    ventas_enero_2022 = []
    ruta = Path(__file__).parent / "datos" / "vivero.csv"

    with open(ruta, "r", encoding="utf-8") as f:
        next(f) # Nos quitamos la cabecera (primera línea) del fichero csv

        for linea in f:
            linea = linea.strip() # Importante quitar el salto de línea al final de cada línea del fichero (y otros espacios en blanco que pueda haber al principio o al final)

            if linea:
                partes = linea.split(",") # En un CSV, cada campo está separado por comas, así que dividimos la línea en partes usando la coma como separador
                id = int(partes[0])
                producto = partes[1]
                dia_str, mes_str, año_str = partes[2].split("/") # la tercera columna (índice 2) es la fecha, es un dato 'compuesto' que tiene formato "dd/mm/yyyy", así que la dividimos usando la barra como separador para obtener día, mes y año por separado
                fecha = datetime(int(año_str), int(mes_str), int(dia_str))
                precio = float(partes[3])

                if es_enero_2022(fecha):
                    venta = Venta(id, producto, fecha, precio)
                    ventas_enero_2022.append(venta)

    # 1. Mostrar ventas
    print("Ventas de enero 2022:")
    for v in ventas_enero_2022:
        print(v)

    # 2. Importe total
    total = sum(v.precio for v in ventas_enero_2022)
    print(f"\nImporte total: {total:.2f}€")

    # 3. Producto más caro
    mas_caro = max(ventas_enero_2022, key=lambda v: v.precio)
    print(f"Producto más caro: {mas_caro.producto} ({mas_caro.precio:.2f}€)")

    # 4. Precio medio
    media = total / len(ventas_enero_2022)
    print(f"Precio medio: {media:.2f}€")x