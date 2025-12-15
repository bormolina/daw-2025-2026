import 'models/Alumno.dart';
import 'models/Asignatura.dart';

void main() {
  Asignatura a1 = Asignatura('Despliegue', 7);
  Asignatura a2 = Asignatura('Servidor', 5);
  Asignatura a3 = Asignatura('Cliente', 5);
  Asignatura a4 = Asignatura('Optativa', 8);

  Alumno alumno = Alumno('Juan Pérez', [a1, a2, a3, a4]);

  print(alumno);

  // Probamos que funciona pendientes()
  print('--- Asignaturas pendientes ---');
  var pendientes = alumno.pendientes();
  if (pendientes.isEmpty) {
    print('No tiene asignaturas pendientes');
  } else {
    pendientes.forEach((a) => print(a));
  }

  // Probar obtieneTitulo()
  print('\n--- Obtención del título ---');
  print('¿Obtiene el título?: ${alumno.obtieneTitulo()}');

  // Probar notaMedia()
  print('\n--- Nota media ---');
  double media = alumno.notaMedia();
  if (media == -1) {
    print('No se puede calcular la nota media porque hay asignaturas suspensas');
  } else {
    print('Nota media: ${media.toStringAsFixed(2)}');
  }
}