import 'dart:io';

void main() {
  Map<String, String> diccionario = {
    "Lista": "Colección ordenada de elementos, accesibles por índices.",
    "Conjunto": "Colección de elementos únicos sin orden predefinido.",
    "Diccionario": "Estructura de datos que almacena pares clave–valor permitiendo acceder rápidamente a los datos asociados a cada clave."
  };

  while (true) {
    stdout.write("Introduce una palabra: ");
    String palabra = stdin.readLineSync() ?? "";

    if (palabra == "salir") {
      print("Chao pescao");
      break;
    }

    String? definicion = diccionario[palabra];

    if (definicion != null) {
      print("$palabra: $definicion\n");
    } else {
      print("La palabra no está en el diccionario\n");
    }
  }
}