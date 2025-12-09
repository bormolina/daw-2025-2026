import 'dart:io';

// Versión clásica
double calcularMediaClasica(List<double> notas) {
  if (notas.isEmpty) return 0;
  double suma = 0;
  for (var n in notas) {
    suma += n;
  }
  return suma / notas.length;
}

String clasificar(double nota) {
  if (nota < 5) {
    return "suspenso";
  } else if (nota < 7) {
    return "aprobado";
  } else if (nota < 9) {
    return "notable";
  } else {
    return "sobresaliente";
  }
}

// Versión funcional
double calcularMediaFuncional(List<double> notas) {
  if (notas.isEmpty) return 0;
  final suma = notas.reduce((a, b) => a + b);
  return suma / notas.length;
}


void main() {
  stdout.write("Introduce las notas separadas por espacios: ");
  final entrada = stdin.readLineSync() ?? "";

  // Convertimos la entrada en una lista de doubles
  final notas = entrada
      .split(" ")
      .map((x) => double.parse(x))
      .toList();

  print("\n--- RESULTADOS ---");

  final media = calcularMediaClasica(notas);
  print("Media del grupo: ${media.toStringAsFixed(2)}");
  for (var n in notas) {
    print("Nota $n → ${clasificar(n)}");
  }

}