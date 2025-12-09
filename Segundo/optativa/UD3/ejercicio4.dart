import 'dart:io';

// Versión funcional (where)

int contar(List<String> xs, String valor) {
  final String e = valor.toLowerCase();
  return xs.where((x) => x.toLowerCase() == e).length;
}


// Versión clásica (bucles for)

int contarClasico(List<String> xs, String valor) {
  final String objetivo = valor.toLowerCase();
  int contador = 0;

  for (String palabra in xs) {
    if (palabra.toLowerCase() == objetivo) {
      contador++;
    }
  }

  return contador;
}

// Programa principal

void main() {
  stdout.write("Introduce palabras separadas por espacios: ");
  String entrada = stdin.readLineSync() ?? "";

  List<String> palabras = entrada
      .split(" ")
      .toList();

  stdout.write("¿Qué palabra quieres contar? ");
  final String valor = stdin.readLineSync() ?? "";

  final int totalFunc = contar(palabras, valor);
  final int totalClas = contarClasico(palabras, valor);

  print("\n--- Versión funcional ---");
  print("La palabra '$valor' aparece $totalFunc veces.");

  print("\n--- Versión clásica ---");
  print("La palabra '$valor' aparece $totalClas veces.\n");
}