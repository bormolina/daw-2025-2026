convocados_espana = [
    "Unai Simón",
    "David Raya",
    "Álex Remiro",
    "Dani Carvajal",
    "Pedro Porro",
    "Robin Le Normand",
    "Pau Cubarsí",
    "Dani Vivian",
    "Dean Huijsen",
    "Marc Cucurella",
    "Alejandro Grimaldo",
    "Rodri",
    "Martín Zubimendi",
    "Mikel Merino",
    "Gavi",
    "Pedri",
    "Fermín López",
    "Fabián Ruiz",
    "Yeremy Pino",
    "Lamine Yamal",
    "Nico Williams",
    "Dani Olmo",
    "Mikel Oyarzabal",
    "Álvaro Morata",
    "Ferran Torres",
    "Jesús Rodríguez"
]

print("Los jugadores cuyo nombre empieza por la misma letra que por la que acaba son: ")
for jugador in convocados_espana:
    if jugador[0].lower() == jugador[len(jugador)-1]:
        print(jugador)