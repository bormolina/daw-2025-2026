import 'dart:io';

void main() {
  Map<String, String> contactos = {
    'Mario': '100123456',
    'Luigi': '111987654',
    'Toad': '122555888',
  };
  bool salir = false;

  while (!salir) {
    print('\nAGENDA');
    print('1. Añadir contacto');
    print('2. Buscar contacto');
    print('3. Listar contactos');
    print('4. Salir');
    stdout.write('Elige una opción: ');

    String opcion = stdin.readLineSync()!;

    switch (opcion) {
      case '1':
        // Añadir contacto
        stdout.write('Nombre: ');
        String nombre = stdin.readLineSync()??''.trim();

        stdout.write('Teléfono: ');
        String telefono = stdin.readLineSync()??''.trim();

        contactos[nombre] = telefono;
        print('Contacto añadido correctamente.');
        break;

      case '2':
        // Buscar contacto
        stdout.write('Introduce el nombre a buscar: ');
        String nombre = stdin.readLineSync()??''.trim();

        if (contactos.containsKey(nombre)) {
          print('Teléfono de $nombre: ${contactos[nombre]}');
        } else {
          print('El contacto no existe.');
        }
        break;

      case '3':
        // Listar contactos
        if (contactos.isEmpty) {
          print('No hay contactos guardados.');
        } else {
          print('\nCOntactos');
          contactos.forEach((nombre, telefono) {
            print('$nombre --> $telefono');
          });
        }
        break;

      case '4':
        salir = true;
        print('Saliendo de la agenda...');
        break;

      default:
        print('Opción no válida.');
    }
  }
}