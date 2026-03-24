from pathlib import Path
import random

class Elemento: # Clase de cada elemento con sus atributos.
    def __init__(self, nombre:str, entrada_simbolo:str, num_atomico:int, masa_atomica:float, grupo:int):
        self.nombre= nombre
        self.entrada_simbolo = entrada_simbolo
        self.num_atomico = num_atomico
        self.masa_atomica = masa_atomica
        self.grupo = grupo



    def __str__(self): #Método para mostrar la informacion de forma legible.
        return f"El elemento: {self.nombre}, tiene como símbolo: {self.entrada_simbolo},  Z = {self.num_atomico} , Masa atómica = {self.masa_atomica} u"

def listado_elementos () -> list:  # transforma el csv en lista de objetos.
    nombre_archivo = Path(__file__).parent.parent /"datos" / "elementos.csv"
    with open(nombre_archivo, "r", encoding="utf-8") as f:
        next(f) #Saltamos el encabezado del csv
        elementos = []
        for linea in f: # Cada linea es un elemento químico.
            nombre, entrada_simbolo, num_atomico, masa_atomica, grupo = linea.strip().split(",") #Divide la lines por comas y asigna a cada variable su valor.
            elemento= Elemento(nombre, entrada_simbolo,  int(num_atomico), float(masa_atomica), int(grupo)) #Crea un objeto de la clase Elemento. 
            elementos.append(elemento) #Anñadimos el objeto a la lista de elementos.
    return elementos
    
    
def jugar(elementos:list):
    while True: 
        print (""" 
Elementos de la Tabla Periódica
            
1. Info a partir del entrada_simbolo del elemento
2. Info a partir del nombre del elemento
3. Jugar
4. Mostrar todos los elementos
0. Salir
                """ )
        opcion = int(input("Elige una opción: "))
        
        if opcion not in range(0,5): # intervalo [0,5) 
            print(f"La opción {opcion} no es válida, elige otra")
        
        if opcion == 0:
            print("Bye, bye")
            break
        
        elif opcion == 1: #Búsqueda del elemento por símbolo.
            entrada_simb = input("Introduce el símbolo del elemento químico: ").strip().lower()
            encontrado = next((e for e in elementos if e.entrada_simbolo.lower() == entrada_simb), None)
            if encontrado:
                print(encontrado)
            else:
                print(f"Elemento {entrada_simb} no encontrado")
        
        elif opcion == 2:  #Búsqueda del elemento por nombre. 
            entrada_nombre = input("Introduce el nombre del elemento químico: ").strip().lower()
            encontrado = next((e for e in elementos if e.nombre.strip().lower() == entrada_nombre), None)
            if encontrado:
                print(encontrado)
            else:
                print(f"Elemento {entrada_nombre} no encontrado")
        
        elif opcion == 3:  #Juego.
            while True:
                print("""
                    1. Adivina el nombre del símbolo del elemento.
                    2. Adivina el símbolo de un elemento
                    3. Jugar con ambos
                    0. Volver al menú principal
                    """)
                sub_opcion = int(input("Elige una opción: "))
                if sub_opcion not in range(0,4):
                    print(f"La opción {sub_opcion} no es válida, elige otra")
                if sub_opcion == 0:
                    break       
                elif sub_opcion == 1:
                    elementos_disponibles = elementos.copy()
                    aciertos = 0

                    while len(elementos_disponibles)> 0: # Bucle hastas que se vacíe las lista de elementos disponibles.
                        elemento = random.choice(elementos_disponibles)# Selecciona objeto al azar.
                        respuesta = input(f"Escribe el nombre de este elemento: {elemento.entrada_simbolo}\n")
                        if respuesta.lower() == elemento.nombre.strip().lower():
                            aciertos +=1
                            print(f"Correcto, llevas {aciertos} aciertos!!")
                            elementos_disponibles.remove(elemento) #Eliminamos objeto de la lista de elementos disponibles.
                        else:
                            print(f"Incorrecto, es {elemento.nombre}. Puntuación obtenida: {aciertos}/{len(elementos)}")
                            break   # Se para el bucle con el primer fallo.
                

                    

                elif sub_opcion == 2:
                    elementos_disponibles = elementos.copy() # Copia d la lista original para ir eliminando ells.
                    aciertos = 0

                    while len(elementos_disponibles)> 0:
                        elemento = random.choice(elementos_disponibles)
                        respuesta = input(f"Escribe el símbolo de este elemento: {elemento.nombre}\n")
                        if respuesta.lower() == elemento.entrada_simbolo.strip().lower():
                            aciertos +=1
                            print(f"Correcto, llevas {aciertos} aciertos!!")
                            elementos_disponibles.remove(elemento)
                        else:
                            print(f"Incorrecto, es {elemento.entrada_simbolo}. Puntuación obtenida: {aciertos}/{len(elementos)}")
                            break
                
                elif sub_opcion == 3:                    
                    elementos_disponibles = elementos.copy()
                    aciertos = 0

                    while len(elementos_disponibles)> 0:
                        elemento = random.choice(elementos_disponibles)
                        opccion = random.choice([1,2]) # Gestion de las preguntas aleatorias.
                        if opccion == 1:
                            respuesta = input(f"Escribe el nombre de este elemento: {elemento.entrada_simbolo}\n")
                            if respuesta.strip().lower() == elemento.nombre.strip().lower():
                                aciertos +=1
                                elementos_disponibles.remove(elemento)

                                print(f"Correcto, llevas {aciertos} aciertos!!")
                                print(f"Elementos restantes: {len(elementos_disponibles)}")
                                if len(elementos_disponibles) == 0:
                                    print(f"¡Enhorabuena! Has acertado todos los elementos. Puntuación final: {aciertos}/{len(elementos)}")
                               
                            else:
                                print(f"Incorrecto, es {elemento.nombre}. Puntuación obtenida: {aciertos}/{len(elementos)}")
                                break   # Se para el bucle con el primer fallo.
                        if opccion == 2:
                            respuesta = input(f"Escribe el símbolo de este elemento: {elemento.nombre}\n")
                            if respuesta.strip().lower() == elemento.entrada_simbolo.strip().lower():
                                aciertos +=1
                                print(f"Correcto, llevas {aciertos} aciertos!!")
                                elementos_disponibles.remove(elemento)
                                print(f"Elementos restantes: {len(elementos_disponibles)}")
                                if len(elementos_disponibles) == 0:
                                    print(f"¡Enhorabuena! Has acertado todos los elementos. Puntuación final: {aciertos}/{len(elementos)}")
                            else:
                                print(f"Incorrecto, es {elemento.entrada_simbolo}. Puntuación obtenida: {aciertos}/{len(elementos)}")
                                break



        elif opcion == 4: 
            for elemento in elementos:
                print(elemento)


        



if __name__ == "__main__":
    elementos = listado_elementos()
    jugar(elementos)    
