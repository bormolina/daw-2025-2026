"""
 Dada una matriz como la siguiente (columna 2 son el número de habitantes y la 4 el área):
paises = [
    ["Argentina", "Buenos Aires", 46000000, "América", 2780400],  
    ["España", "Madrid", 48000000, "Europa", 505990],  
    ["Japón", "Tokio", 125000000, "Asia", 377975],  
    ["Sudáfrica", "Pretoria", 60000000, "África", 1221037],  
    ["Australia", "Canberra", 26000000, "Oceanía", 7692024],  
    ["Canadá", "Ottawa", 38000000, "América", 9984670]  
]

Crea una función que recibido un continente y la lista de países devuelva el país con mayor densidad de población (población/área) del continente.
"""

def mas_plabado_continente(paises: list[list], continente: str) -> list:
    # Primero me quedo con los países del continente 
    paises_continente = [pais for pais in paises if pais[3] == continente]

    # Me quedo con el país de mayor densidad
    # Comienzo suponinedo que es el primero
    # Y recorro todos los demás buscando si hay alguno de mayor densidad
    pais_mas_densidad = paises_continente[0]
    max_densidad = pais_mas_densidad[2] / pais_mas_densidad[4]
    for pais in paises_continente:
        if max_densidad < pais[2] / pais[4]:
            pais_mas_densidad = pais

    return pais_mas_densidad

paises = [
    ["Argentina", "Buenos Aires", 46000000, "América", 2780400],  
    ["España", "Madrid", 48000000, "Europa", 505990],
    ["Japón", "Tokio", 125000000, "Asia", 377975],  
    ["Sudáfrica", "Pretoria", 60000000, "África", 1221037],  
    ["Australia", "Canberra", 26000000, "Oceanía", 7692024],  
    ["Canadá", "Ottawa", 38000000, "América", 9984670]  
]

print(mas_plabado_continente(paises, "Europa"))