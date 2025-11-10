# Lista con los nombres de los planetas del sistema solar
planetas_sistema_solar = [
   "Mercurio", "Venus", "Tierra", "Marte",
   "Júpiter", "Saturno", "Urano", "Neptuno"
]


# Lista con las masas de los planetas en kilogramos (valores aproximados)
masas_sistema_solar = [
   3.3011e23,  # Mercurio
   4.8675e24,  # Venus
   5.97237e24, # Tierra
   6.4171e23,  # Marte
   1.8982e27,  # Júpiter
   5.6834e26,  # Saturno
   8.6810e25,  # Urano
   1.02413e26  # Neptuno
]

# Encuentro el planeta más pesado (y me olvido de encontrar los que pesan más que la media)
mas_pesado = planetas_sistema_solar[0]
masa_mayor = masas_sistema_solar[0]

for i, masa in enumerate(masas_sistema_solar):
    if masa > masa_mayor:
        masa_mayor = masa
        mas_pesado = i

print(f"El planeta más pesado es {planetas_sistema_solar[mas_pesado]} que pesa {masa_mayor} kg")

# Encuentro que planetas pesas más que la media

sumatoria = 0

for masa in masas_sistema_solar:
    sumatoria += masa

masa_media = sumatoria / len(masas_sistema_solar)

for i, masa in enumerate(masas_sistema_solar):
    if masa > masa_media:
        print(f"{planetas_sistema_solar[i]} pesa {masa} más que la media {masa_media}")