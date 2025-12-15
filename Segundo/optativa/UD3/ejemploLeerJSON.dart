import 'dart:convert';
import 'dart:io';
import 'models/Grafica.dart';

void main() {
  File file = File('data/graficas.json');

  try {
    // Leer todo el contenido del fichero JSON
    String contenido = file.readAsStringSync();

    // Convertir el texto JSON en una estructura Dart
    List<dynamic> datos = jsonDecode(contenido);

    // Convertir cada elemento del JSON en un objeto Grafica
    List<Grafica> graficas = datos
        .map((e) => Grafica.fromJson(e))
        .toList();

    // Mostrar las gráficas leídas
    for (var g in graficas) {
      print(g);
    }
  } catch (e) {
    print('Error al leer el fichero JSON');
  }
}