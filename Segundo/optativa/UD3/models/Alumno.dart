import 'Asignatura.dart';

class Alumno {
  String nombre;
  List<Asignatura> asignaturas;

  Alumno(this.nombre, this.asignaturas);

  List<Asignatura> pendientes() {
    return asignaturas.where((a) => !a.aprobado()).toList();
  }

  bool obtieneTitulo() {
    return asignaturas.every((a) => a.aprobado());
  }

  /// Devuelve la nota media si no hay pendientes.
  /// Si hay alguna asignatura suspensa, devuelve -1.
  double notaMedia() {
    if (!obtieneTitulo()) {
      return -1;
    }

    int suma = asignaturas.fold(0, (acc, a) => acc + a.nota);
    return suma / asignaturas.length;
  }

  @override
  String toString() {
    String resultado = 'Alumno: $nombre\nAsignaturas:\n';

    for (Asignatura a in asignaturas) {
      resultado += '  - ${a.toString()}\n';
    }

    return resultado;
  }
}