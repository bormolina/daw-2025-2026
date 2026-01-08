import 'dart:io';

void main() {
  File entrada = File('registro.txt');
  File salida = File('registro_corregido.txt');

  List<String> lineas = entrada.readAsLinesSync();
  List<String> resultado = [];

  bool aplicarSobreprecio = false;
  double dineroPerdido = 0.0;

  for (String linea in lineas) {
    // Línea de fecha
    if (linea.startsWith('#')) {
      // Activar o desactivar el sobreprecio según la fecha
      if (linea == '#04/11/2025') {
        aplicarSobreprecio = true;
      } else if (linea == '#10/11/2025') {
        aplicarSobreprecio = false;
      }

      resultado.add(linea);
    }
    // Línea vacía
    else if (linea.trim().isEmpty) {
      resultado.add(linea);
    }
    // Línea producto:precio
    else {
      List<String> partes = linea.split(':');
      String nombre = partes[0];
      double precio = double.parse(partes[1]);

      if (aplicarSobreprecio) {
        double incremento = precio * 0.12;
        dineroPerdido += incremento;
        precio += incremento;
      }

      resultado.add('$nombre:${precio.toStringAsFixed(2)}');
    }
  }

  salida.writeAsStringSync(resultado.join('\n'));

  print(
    'Dinero perdido por no aplicar el sobreprecio: ${dineroPerdido.toStringAsFixed(2)} €'
  );
}