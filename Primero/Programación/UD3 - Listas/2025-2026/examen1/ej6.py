def cuenta_palabras(txt: str) -> list[tuple[str, int]]:
    txt_lista = [p.lower() for p in txt.split()]
    txt_sin_repes = list(set(txt_lista))
    reporte = []
    for palabra in txt_sin_repes:
        reporte.append((palabra, txt_lista.count(palabra)))
    return reporte


def imprimir_reporte(reporte: list[tuple[str, int]]):
    for palabra, n in reporte:
        print(f'Palabra: {palabra} | nº veces: {n}')

texto_quijote = 'En un lugar de la Mancha de cuyo nombre no quiero acordarme no ha mucho tiempo que vivía un hidalgo de los de lanza en astillero adarga antigua rocín flaco y galgo corredor'

imprimir_reporte(cuenta_palabras(texto_quijote))
