precipitaciones_granada_2023 = [
   40.2,  # Enero
   35.6,  # Febrero
   45.8,  # Marzo
   50.1,  # Abril
   30.3,  # Mayo
   10.4,  # Junio
   1.2,   # Julio
   5.6,   # Agosto
   20.8,  # Septiembre
   60.5,  # Octubre
   55.3,  # Noviembre
   42.7   # Diciembre
]

sumatoria = 0

for p in precipitaciones_granada_2023:
    sumatoria += p

media = sumatoria / len(precipitaciones_granada_2023)

print(f"La precipitación media de Granada es {media:.2f} l/m²")
