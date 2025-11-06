paises_europa = [
    "Albania",
    "Alemania",
    "Andorra",
    "Armenia",
    "Austria",
    "Azerbaiyán",
    "Bélgica",
    "Bielorrusia",
    "Bosnia y Herzegovina",
    "Bulgaria",
    "Chipre",
    "Croacia",
    "Dinamarca",
    "Eslovaquia",
    "Eslovenia",
    "España",
    "Estonia",
    "Finlandia",
    "Francia",
    "Georgia",
    "Grecia",
    "Hungría",
    "Irlanda",
    "Islandia",
    "Italia",
    "Kazajistán",  # parcialmente en Europa
    "Kosovo",
    "Letonia",
    "Liechtenstein",
    "Lituania",
    "Luxemburgo",
    "Malta",
    "Moldavia",
    "Mónaco",
    "Montenegro",
    "Noruega",
    "Países Bajos",
    "Polonia",
    "Portugal",
    "Reino Unido",
    "República Checa",
    "Rumania",
    "Rusia",  # parcialmente en Europa
    "San Marino",
    "Serbia",
    "Suecia",
    "Suiza",
    "Turquía",  # parcialmente en Europa
    "Ucrania",
    "Ciudad del Vaticano"
]

print("Los paises de Europa con 6 o menos letras son: ")
for pais in paises_europa:
    if len(pais) <= 6:
        print(pais)
