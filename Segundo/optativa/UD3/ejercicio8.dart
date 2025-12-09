import 'dart:io';

List<int> fibonacci(int n) {

  List<int> serie = [];
  for (int i = 0; i < n; i++) {
    if (i == 0) {
      serie.add(0);
    } else if (i == 1) {
      serie.add(1);
    } else {
      serie.add(serie[i - 1] + serie[i - 2]);
    }
  }
  return serie;
}

void main() {
  int termino = 0;
  print('Inserta el número de términos de la serie Fibonacci que deseas generar (debe ser positivo): ');
  while (termino <= 0) {
    termino = int.parse(stdin.readLineSync() ?? "0");
    if(termino<=0) print('El término no puede ser cero o negativo. Inténtalo de nuevo: ');
  }

  List<int> serieFibo = fibonacci(termino);
  print('Los primeros $termino términos de la serie Fibonacci son: $serieFibo');
  int sumaTotal = serieFibo.fold(0, (a, b) => a + b);
  print('La suma total de estos términos es: $sumaTotal');
}