import 'dart:io';

bool esContrasenaValida(String s) {
  final bool tieneLongitud = s.length >= 8;
  final bool tieneMayus = s.contains(RegExp(r'[A-Z]'));
  final bool tieneMinus = s.contains(RegExp(r'[a-z]'));
  final bool tieneNumero = s.contains(RegExp(r'[0-9]'));

  return tieneLongitud && tieneMayus && tieneMinus && tieneNumero;
}

void main() {

  while (true) {
    stdout.write("Contraseña: ");
    final input = stdin.readLineSync() ?? "";

    if (esContrasenaValida(input)) {
      print("Contraseña válida.");
      break;
    } else {
      print("Contraseña no válida. Inténtalo de nuevo.\n");
    }
  }
}

// Para pensar. Cómo podríamos hacer que la función devuelva qué requisitos no se cumplen?