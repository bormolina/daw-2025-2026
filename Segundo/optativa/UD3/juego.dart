import 'dart:io';
import 'dart:math';

void jugar() {
  Random rnd = Random();
  int racha = 0;

  while (true) {
    int a = rnd.nextInt(10) + 1;
    int b = rnd.nextInt(10) + 1;

    stdout.write('Cuanto es $a x $b? ');
    String? respuesta = stdin.readLineSync();

    int? valor = int.tryParse(respuesta ?? '');

    if (valor == a * b) {
      racha++;
      print('Correcto. Racha: $racha');
    } else {
      print('Incorrecto. La respuesta era ${a * b}');
      print('Racha final: $racha');
      actualizarRecord(racha);
      break;
    }
  }
}

void verRecord() {
  int record = leerRecord();
  print('\nRecord actual: $record');
}

int leerRecord() {
  File file = File('data/records.txt');

  if (!file.existsSync()) {
    return 0;
  }

  String contenido = file.readAsStringSync().trim();
  return int.tryParse(contenido) ?? 0;
}

void actualizarRecord(int nuevaRacha) {
  File file = File('data/records.txt');
  int recordActual = leerRecord();

  if (nuevaRacha > recordActual) {
    file.writeAsStringSync(nuevaRacha.toString());
    print('Nuevo record guardado');
  } else {
    print('El record sigue siendo $recordActual');
  }
}

void main() {
  while (true) {
    print('\nMENU');
    print('1. Jugar');
    print('2. Ver record');
    print('0. Salir');
    stdout.write('Opcion: ');

    String? opcion = stdin.readLineSync();

    if (opcion == '1') {
      jugar();
    } else if (opcion == '2') {
      verRecord();
    } else if (opcion == '0') {
      break;
    } else {
      print('Opcion no valida');
    }
  }
}