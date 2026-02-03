from Pedido import Pedido
from datetime import datetime


def get_datos() -> list[Pedido]:
    return [
        Pedido(1, "Cerezo", 800, ["Calle Real", 5, "Monachil"],
               datetime(2024, 1, 10), datetime(2024, 1, 15), 520, "Manolito"),

        Pedido(2, "Almendro", 450, ["Calle Granada", 12, "Cájar"],
               datetime(2024, 1, 12), datetime(2024, 1, 18), 310, "Raulito"),

        Pedido(3, "Olivo", 1200, ["Camino del Río", 3, "Huétor Vega"],
               datetime(2024, 1, 14), datetime(2024, 1, 20), 900, "Manolito"),

        Pedido(4, "Cerezo", 600, ["Calle Alta", 7, "La Zubia"],
               datetime(2024, 1, 16), datetime(2024, 1, 22), 430, "Juanillo"),

        Pedido(5, "Almendro", 300, ["Calle Ancha", 9, "Granada"],
               datetime(2024, 1, 18), datetime(2024, 1, 23), 210, "Manolito"),

        Pedido(6, "Olivo", 950, ["Calle Molino", 4, "Monachil"],
               datetime(2024, 1, 20), datetime(2024, 1, 25), 700, "Raulito"),

        Pedido(7, "Cerezo", 500, ["Calle Baja", 11, "Cájar"],
               datetime(2024, 1, 22), datetime(2024, 1, 27), 360, "Manolito"),

        Pedido(8, "Almendro", 780, ["Camino Viejo", 2, "Huétor Vega"],
               datetime(2024, 1, 24), datetime(2024, 1, 30), 540, "Pepillo"),

        Pedido(9, "Olivo", 1100, ["Calle Nueva", 8, "La Zubia"],
               datetime(2024, 1, 26), datetime(2024, 2, 1), 820, "Manolito"),

        Pedido(10, "Cerezo", 400, ["Calle Recogidas", 15, "Granada"],
                datetime(2024, 1, 28), datetime(2024, 2, 2), 290, "Antoñico"),

        Pedido(11, "Almendro", 650, ["Calle Acequia", 6, "Monachil"],
               datetime(2024, 2, 1), datetime(2024, 2, 6), 470, "Raulito"),

        Pedido(12, "Olivo", 900, ["Calle Jardines", 10, "Cájar"],
               datetime(2024, 2, 3), datetime(2024, 2, 8), 680, "Manolito"),

        Pedido(13, "Cerezo", 350, ["Camino Alto", 1, "Huétor Vega"],
               datetime(2024, 2, 5), datetime(2024, 2, 6), 260, "Raulito"),

        Pedido(14, "Almendro", 720, ["Calle Sol", 14, "La Zubia"],
               datetime(2024, 2, 7), datetime(2024, 2, 12), 510, "Juanillo"),

        Pedido(15, "Olivo", 1000, ["Calle Pedro Antonio", 20, "Granada"],
               datetime(2024, 2, 9), datetime(2024, 2, 14), 760, "Manolito"),

        Pedido(16, "Cerezo", 480, ["Calle Nogal", 3, "Monachil"],
               datetime(2024, 2, 11), datetime(2024, 2, 16), 350, "Raulito"),

        Pedido(17, "Almendro", 850, ["Calle Sierra", 9, "Cájar"],
               datetime(2024, 2, 13), datetime(2024, 2, 18), 620, "Manolito"),

        Pedido(18, "Olivo", 1300, ["Camino Verde", 7, "Huétor Vega"],
               datetime(2024, 2, 15), datetime(2024, 2, 20), 980, "Raulito"),

        Pedido(19, "Cerezo", 550, ["Calle Luna", 4, "La Zubia"],
               datetime(2024, 2, 17), datetime(2024, 2, 22), 400, "Pepillo"),

        Pedido(20, "Olivo", 350, ["Calle Profesor Borja", 1, "Monachil"],
               datetime(2024, 1, 1), datetime(2024, 3, 1), 210, "Manolito"),
    ]


def get_datos_competencia() -> list[Pedido]:
    return [
        Pedido(1001, "Olivo", 700, ["Calle Real", 3, "Monachil"],
               datetime(2024, 1, 11), datetime(2024, 1, 16), 500, "El Chacho"),

        Pedido(1002, "Cerezo", 480, ["Camino del Río", 6, "Cájar"],
               datetime(2024, 1, 13), datetime(2024, 1, 19), 380, "El Chacho"),

        Pedido(1003, "Almendro", 520, ["Calle Granada", 14, "Granada"],
               datetime(2024, 1, 15), datetime(2024, 1, 21), 360, "El Bigotes"),

        Pedido(1004, "Olivo", 950, ["Calle Alta", 2, "La Zubia"],
               datetime(2024, 1, 17), datetime(2024, 1, 24), 720, "El Bigotes"),

        Pedido(1005, "Cerezo", 300, ["Camino Viejo", 5, "Huétor Vega"],
               datetime(2024, 1, 19), datetime(2024, 1, 25), 240, "El Chacho"),

        Pedido(1006, "Almendro", 650, ["Calle Sol", 11, "Cájar"],
               datetime(2024, 1, 21), datetime(2024, 1, 27), 470, "El Moreno"),

        Pedido(1007, "Olivo", 1100, ["Calle Nueva", 9, "Granada"],
               datetime(2024, 1, 23), datetime(2024, 1, 30), 850, "El Moreno"),

        Pedido(1008, "Cerezo", 560, ["Calle Luna", 4, "La Zubia"],
               datetime(2024, 1, 25), datetime(2024, 2, 1), 430, "El Bigotes"),

        Pedido(1009, "Almendro", 400, ["Calle Profesor Borja", 1, "Monachil"],
               datetime(2024, 1, 27), datetime(2024, 2, 2), 300, "El Chacho"),

        Pedido(1010, "Olivo", 850, ["Calle Jardines", 6, "Cájar"],
               datetime(2024, 1, 29), datetime(2024, 2, 4), 650, "El Moreno"),

        Pedido(1011, "Cerezo", 420, ["Calle Arabial", 18, "Granada"],
               datetime(2024, 2, 1), datetime(2024, 2, 6), 330, "El Bigotes"),

        Pedido(1012, "Olivo", 900, ["Calle Recogidas", 22, "Granada"],
               datetime(2024, 2, 3), datetime(2024, 2, 8), 700, "El Moreno"),

        Pedido(1013, "Almendro", 500, ["Calle Pedro Antonio", 10, "Granada"],
               datetime(2024, 2, 5), datetime(2024, 2, 10), 380, "El Chacho"),

        Pedido(1014, "Cerezo", 360, ["Camino de Ronda", 55, "Granada"],
               datetime(2024, 2, 7), datetime(2024, 2, 12), 290, "El Bigotes"),

        Pedido(1015, "Olivo", 1000, ["Calle Emperatriz Eugenia", 7, "Granada"],
               datetime(2024, 2, 9), datetime(2024, 2, 14), 780, "El Moreno"),
    ]