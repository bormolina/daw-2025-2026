animales_mitologicos = [
   "Yeti",
   "Monstruo del lago Ness",
   "Mokele-mbembe",
   "Chupacabras",
   "Aberroncho",
   "Hombre polilla",
   "Demonio de Dover",
   "Mapinguarí",
   "Nahuelito",
   "Kraken",
   "Wendigo",
   "Ahool",
   "Jersey Devil",
   "Skinwalker",
   "Ogopogo",
   "Borja profe de programación"
]

print('Listado de animales con nombre compuesto: ')
for animal in animales_mitologicos:
    if len(animal.split()) > 1:
        print(f"\t{animal}")

