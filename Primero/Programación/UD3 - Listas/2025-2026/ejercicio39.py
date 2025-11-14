palabras_txt = input('Inserta palabras separadas por ,: ')
palabras = palabras_txt.split(',')

mas_larga = palabras[0]
mas_corta = palabras[0]

for palabra in palabras:
    if len(palabra) > len(mas_larga):
        mas_larga = palabra

    if len(palabra) < len(mas_corta):
        mas_corta = palabra

print(f"La palabra más larga es: {mas_larga}")
print(f"La palabra más corta es: {mas_corta}")


