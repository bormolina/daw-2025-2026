class Asignatura {
  String nombre;
  int nota;

  Asignatura(this.nombre, this.nota);

  bool aprobado() {
    return nota >= 5;
  }

  String rangoNota() {
    if (nota >= 0 && nota <= 4) {
      return 'Suspenso';
    } else if (nota == 5) {
      return 'Suficiente';
    } else if (nota == 6) {
      return 'Bien';
    } else if (nota >= 7 && nota <= 8) {
      return 'Notable';
    } else if (nota >= 9 && nota <= 10) {
      return 'Sobresaliente';
    } else {
      return 'Nota inválida';
    }
  }

  @override
  String toString() {
    return 'Asignatura(nombre: $nombre, nota: $nota, rango: ${rangoNota()})';
  }
}