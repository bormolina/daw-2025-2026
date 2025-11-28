from random import randint

def generar_nota()->str:
    notas = ['DO', 'RE', 'MI', 'FA', 'SOL', 'LA', 'SI']
    return notas[randint(0, len(notas)-1)]

def generar_partitura(longitud: int, nRepes: int) -> list[str]:
    if longitud == 0:
        return []
    
    if longitud == 1:
        return [generar_nota()]
    
    partitura = [generar_nota()]
    racha = 1

    while len(partitura) < longitud:
        if racha < nRepes:
            partitura.append(generar_nota())
        else:
            candidata = generar_nota()
            while candidata == partitura[-1]:
                candidata = generar_nota()
            partitura.append(candidata)
        
        if partitura[-1] == partitura[-2]:
            racha += 1
        else:
            racha = 1
    
    return partitura


print(generar_partitura(20, 2))