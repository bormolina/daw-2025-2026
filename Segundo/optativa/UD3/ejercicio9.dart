import 'dart:io';


List<String> palabras(String s) {
  return s.split(" ").map((p) => p.trim()).toList();
}

double longitudMedia(List<String> xs) {
  int suma = xs.fold(0, (acc, p) => acc + p.length);
  return suma / xs.length;
}

List<String> topLargas(List<String> xs, int k) {
  List<String> copia = List.from(xs);
  copia.sort((a, b) => b.length.compareTo(a.length));
  List<String> resultado = [];
  for (int i = 0; i < k && i < copia.length; i++) {
    resultado.add(copia[i]);
  }

  return resultado;
}

void main() {
  stdout.write("Introduce un texto: ");
  String texto = stdin.readLineSync() ?? "";
  List<String> lista = palabras(texto);

  print("Total de palabras: ${lista.length}");
  print("Longitud media: ${longitudMedia(lista).toStringAsFixed(2)}");

  List<String> top3 = topLargas(lista, 3);
  print("Las 3 palabras más largas: ${top3.join(', ')}");
}