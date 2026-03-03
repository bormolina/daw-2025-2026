from datos import get_productos

productos = get_productos()

resultado = {}

# Calculo el número de productos y la sumatoria
for p in productos:
    for cat in p.categorias:
        datos_cat = resultado.get(cat, {"num_productos": 0, "precio_medio": 0.0})
        datos_cat["num_productos"] += 1
        datos_cat["precio_medio"] += p.precio
        resultado[cat] = datos_cat

# Calculo la media
for cat in resultado:
    num = resultado[cat]["num_productos"]
    resultado[cat]["precio_medio"] = resultado[cat]["precio_medio"] / num

# Muestro los resultado
for cat in resultado:
    print(f"{cat} -- Número productos: {resultado[cat]['num_productos']} -- Precio medio: {resultado[cat]['precio_medio']:.2f}€")
