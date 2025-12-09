import 'dart:io';

// Versión clásica
double mediaSemanalClasica(List<double> temps) {
  if (temps.isEmpty) return 0;
  double suma = 0;
  for (double t in temps) {
    suma += t;
  }
  return suma / temps.length;
}

// Alternativa funcional
double mediaSemanalFuncional(List<double> temps) {
  if (temps.isEmpty) return 0;
  final suma = temps.reduce((a, b) => a + b);
  return suma / temps.length;
}

// FUNCIÓN 2: diasCalurosos (devolver índices)

// Versión clásica
List<int> diasCalurososClasica(List<double> temps, double umbral) {
  List<int> indices = [];
  for (int i = 0; i < temps.length; i++) {
    if (temps[i] > umbral) {
      indices.add(i);
    }
  }
  return indices;
}

// Versión funcional
List<int> diasCalurososFuncional(List<double> temps, double umbral) {
  // List.generate(n, (i) => i) crea una lista de 0 a n-1 generando cada elemento a partir de su índice.
  // FULL FUNCIONAL
  return List.generate(temps.length, (i) => i)
      .where((i) => temps[i] > umbral)
      .toList();
}


void main() {
  print("Introduce las 7 temperaturas diarias separadas por espacios:");
  final String entrada = stdin.readLineSync() ?? "";

  final List<double> temps = entrada
      .split(" ")
      .map((x) => double.parse(x))
      .toList();


  stdout.write("Introduce el umbral de calor: ");
  final double umbral = double.parse(stdin.readLineSync() ?? "0");


  final double media = mediaSemanalClasica(temps);
  print("Media semanal: ${media.toStringAsFixed(2)} ºC");

  // Días calurosos
  final List<int> dias = diasCalurososClasica(temps, umbral);

  if (dias.isEmpty) {
    print("No hay días por encima del umbral.");
  } else {
    print("Días calurosos (índices 0-6): $dias");
  }
}