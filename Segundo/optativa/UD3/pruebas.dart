void main() {
  List<int> numeros = [1, 2, 3, 4, 5];

  // forEach: ejecuta una acción sobre cada elemento (no devuelve nada)
  print('forEach:');
  numeros.forEach((int n) => print('Número: $n'));
``
  // map: transforma cada elemento y devuelve una nueva lista
  List<int> cuadrados = numeros.map((int n) => n * n).toList();
  print('map -> cuadrados: $cuadrados');

  // where: filtra los elementos que cumplen una condición
  List<int> pares = numeros.where((int n) => n % 2 == 0).toList();
  print('where -> pares: $pares');

  // reduce: combina los elementos en un único valor (sin valor inicial)
  int suma = numeros.reduce((int acum, int n) => acum + n);
  print('reduce -> suma total: $suma');

  // fold: igual que reduce, pero permite un valor inicial y tipo distinto
  int producto = numeros.fold<int>(1, (int acum, int n) => acum * n);
  print('fold -> producto total: $producto');

  // any: devuelve true si algún elemento cumple la condición
  bool hayMayores = numeros.any((int n) => n > 4);
  print('any -> ¿hay algún número > 4?: $hayMayores');

  // every: devuelve true si todos los elementos cumplen la condición
  bool todosPositivos = numeros.every((int n) => n > 0);
  print('every -> ¿todos son positivos?: $todosPositivos');
}