paises = ["Alemania", "Francia", "Italia", "España", "Países Bajos", "Polonia", "Suecia", "Bélgica", "Austria", "Portugal"]
poblaciones = [83, 68, 59, 47, 17, 38, 10, 11, 9, 10]  # En millones de habitantes

menorPoblacion = min(poblaciones)
media = sum(poblaciones) / len(poblaciones)

print(f'La media de la poblacion es {media} \n'
      f'El pais con menor poblacion es {paises[poblaciones.index(menorPoblacion)]}')