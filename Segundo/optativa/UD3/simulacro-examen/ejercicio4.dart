import 'dart:convert';
import 'dart:io';
import 'Producto.dart';

void main() {
  // Leer el fichero JSON
  File fichero = File('inventario.json');
  String contenido = fichero.readAsStringSync();

  // Decodificar el JSON
  List<dynamic> datos = jsonDecode(contenido);

  // Crear la lista de productos usando fromJson
  List<Producto> productos = [];

  for (Map<String, dynamic> prodJson in datos) {
    productos.add(Producto.fromJson(prodJson));
  }

  // A) Mostrar todos los productos
  print('--- LISTA COMPLETA DE PRODUCTOS ---');
  productos.forEach(print);

  // B) Mostrar el 15% de los productos más caros
  productos.sort((a, b) => b.precio.compareTo(a.precio));

  int cantidad = (productos.length * 0.15).ceil();

  print('\n 15% DE LOS PRODUCTOS MÁS CAROS');
  for (int i = 0; i < cantidad; i++) {
    print(productos[i]);
  }
}