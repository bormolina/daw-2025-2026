diccionario = {
    'dog': 'perro',
    'cat': 'gato',
    'tear': 'lágrima',
    'pedestrian': 'peatón'
}

while True:
    ingles = input('Palabra en inglés? ')
    if ingles in diccionario:
        print(f'Traducción: {diccionario.get(ingles)}')
    else:
        print('La palabra no está en el diccionario')
        espanhol = input('Traducción en español? ')
        diccionario[ingles] = espanhol