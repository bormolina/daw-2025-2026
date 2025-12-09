List<double> aplicarDescuento(List<double> precios, double porcentaje) {
  List<double> rebajados = [];
  for (double p in precios) {
    rebajados.add(p - p * porcentaje / 100);
  }
  return rebajados;
}

double total(List<double> precios) {
  double suma = 0;
  for (double p in precios) {
    suma += p;
  }

  // Si supera 100€, aplicar descuento del 10%
  if (suma > 100) {
    suma = suma * 0.90;
  }

  return suma;
}

void main() {
  List<double> precios = [25.0, 40.0, 15.0, 30.0, 40.5];

  double totalAntes = precios.fold(0, (double acc, double p) => acc + p);
  print("Total antes del descuento: €$totalAntes");

  // Aplicar descuento del 2%
  List<double> preciosRebajados = aplicarDescuento(precios, 2);
  // Calculamos el precio final
  double totalFinal = total(preciosRebajados);
  print("Total final: €$totalFinal");
  print("Ahorro: €${totalAntes - totalFinal}");
}