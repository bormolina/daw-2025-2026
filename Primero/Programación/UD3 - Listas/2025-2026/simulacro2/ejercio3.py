pokemones = [
   ["Pikachu", ["Eléctrico"]],
   ["Charmander", ["Fuego"]],
   ["Bulbasaur", ["Planta", "Veneno"]],
   ["Squirtle", ["Agua"]],
   ["Gengar", ["Fantasma", "Veneno"]],
   ["Onix", ["Roca", "Tierra"]],
   ["Machamp", ["Lucha"]],
   ["Zapdos", ["Eléctrico", "Volador"]],
   ["Dragonite", ["Dragón", "Volador"]],
   ["Eevee", ["Normal", "Eléctrico"]]
]

electricos = [p[0] for p in pokemones if 'Eléctrico' in p[1]]
print(electricos)

electricos_dobles = [p[0] for p in pokemones if 'Eléctrico' in p[1] and len(p[1]) > 1]
print(electricos_dobles)