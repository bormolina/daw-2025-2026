import 'dart:io';

void main() {
  // Diccionario de países y capitales
  Map<String, String> capitales = {
    'España': 'Madrid',
    'Francia': 'París',
    'Italia': 'Roma',
    'Alemania': 'Berlín',
    'Portugal': 'Lisboa',
  };

  int aciertos = 0;
  int total = capitales.length;

  print('Juego de las capitales');

  capitales.forEach((pais, capital) {
    stdout.write('Capital de $pais --> ');
    String respuesta = stdin.readLineSync() ?? ''.trim();

    if (respuesta.toLowerCase() == capital.toLowerCase()) {
      print('Correcto');
      aciertos++;
    } else {
      print('Incorrecto (era $capital)');
    }
  });

  print('\nResultado final:');
  print('Has acertado $aciertos de $total preguntas.');
}