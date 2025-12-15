class Grafica {
  String modelo;
  String fabricante;
  int memoriaGb;
  String tipoMemoria;
  int consumoW;
  int precioEur;

  Grafica(
    this.modelo,
    this.fabricante,
    this.memoriaGb,
    this.tipoMemoria,
    this.consumoW,
    this.precioEur,
  );

  // Se usa 'factory' porque este constructor NO crea los datos desde cero,
  // sino que construye un objeto Grafica a partir de un Map (JSON ya leído).
  // Es una forma habitual de convertir datos externos en objetos.
  factory Grafica.fromJson(Map<String, dynamic> json) {

    // 'dynamic' se usa porque los valores del JSON no tienen tipo fijo en Dart.
    // El JSON puede contener strings, números, booleanos, etc., y Dart
    // no puede saber su tipo exacto en tiempo de compilación.
    return Grafica(
      json['modelo'],
      json['fabricante'],
      json['memoria_gb'],
      json['tipo_memoria'],
      json['consumo_w'],
      json['precio_eur'],
    );
  }

  @override
  String toString() {
    return 'Grafica(modelo: $modelo, fabricante: $fabricante, '
           'memoria: ${memoriaGb}GB $tipoMemoria, '
           'consumo: ${consumoW}W, precio: ${precioEur}€)';
  }
}