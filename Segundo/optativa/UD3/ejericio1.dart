/*
Escribe un programa que lea números enteros desde teclado y los guarde en una lista hasta que el usuario introduzca un 0. Después, el programa debe mostrar únicamente los números pares. Para ello, crea una función llamada esPar(int n) -> bool que devuelva un valor booleano indicando si el número recibido es par o no, y utilízala dentro del programa principal para filtrar la lista antes de mostrarla.
*/

import 'dart:io';

bool esPar(int n){
  return n % 2 == 0;
}

void main(){
  List<int> nums = [];

  while (true){
    print('Inserta un número: ');
    int n = int.parse(stdin.readLineSync() ?? '');

    if(n==0){
      break;
    }

    nums.add(n);
  }

  List<int> pares = nums.where((n) => esPar(n)).toList();
  print('Los numeros pares son $pares');
}