import 'dart:io';


// VERSION FUNCIONAL (where / map) 

List<int> filtrarMayores(List<int> xs, int umbral) {
  return xs.where((x) => x > umbral).toList();
}

List<int> cuadrados(List<int> xs) {
  return xs.map((x) => x * x).toList();
}


// VERSION CLÁSICA (bucles for)

List<int> filtrarMayoresClasico(List<int> xs, int umbral) {
  List<int> res = [];
  for (int x in xs) {
    if (x > umbral) {
      res.add(x);
    }
  }
  return res;
}

List<int> cuadradosClasico(List<int> xs) {
  List<int> res = [];
  for (int x in xs) {
    res.add(x * x);
  }
  return res;
}

// PROGRAMA PRINCIPAL

void main() {
  stdout.write("Introduce números separados por espacios: ");
  String entradaNums = stdin.readLineSync() ?? "";

  // Ejemplo claro de progrmación funcional: fíjate como se concatenan métodos de las listas
  List<int> numeros = entradaNums
      .split(" ")
      .map((e) => int.parse(e))
      .toList();

  stdout.write("Introduce un valor umbral: ");
  String entradaUmbral = stdin.readLineSync() ?? "0";
  final int umbral = int.parse(entradaUmbral);

  // Llamadas a funciones con enfoque funcional
  List<int> mayoresFunc = filtrarMayores(numeros, umbral);
  List<int> cuadradosFunc = cuadrados(mayoresFunc);

  print("\n--- Versión funcional ---");
  print("Números mayores que $umbral: $mayoresFunc");
  print("Cuadrados: $cuadradosFunc");

  // Llamadas a funciones con enfoque clásico
  List<int> mayoresClas = filtrarMayoresClasico(numeros, umbral);
  List<int> cuadradosClas = cuadradosClasico(mayoresClas);

  print("\n--- Versión clásica ---");
  print("Números mayores que $umbral: $mayoresClas");
  print("Cuadrados: $cuadradosClas\n");
}