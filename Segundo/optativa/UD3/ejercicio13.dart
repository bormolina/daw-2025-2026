import 'models/Coche.dart';

List<Coche> soloAutomaticos(List<Coche> xs) {
  return xs.where((c) => c.automatico).toList();
}

List<Coche> posterioresA(List<Coche> xs, int anio) {
  return xs.where((c) => c.anio_fabricacion > anio).toList();
}

List<Coche> topAutonomia(List<Coche> xs, int k) {
  List<Coche> copia = List.from(xs);

  copia.sort((a, b) => b.autonomia().compareTo(a.autonomia()));

  if (k > copia.length) {
    k = copia.length;
  }

  return copia.sublist(0, k);
}

double potenciaMediaMarca(List<Coche> xs, String marca) {
  List<Coche> filtrados =
      xs.where((c) => c.marca.toLowerCase() == marca.toLowerCase()).toList();

  if (filtrados.isEmpty) {
    return 0;
  }

  int suma = filtrados.fold(0, (acc, c) => acc + c.potencia);

  return suma / filtrados.length;
}

void reducirConsumo(List<Coche> xs, double porcentaje) {
  for (var c in xs) {
    double reduccion = c.consumo * (porcentaje / 100);
    c.consumo -= reduccion;

    if (c.consumo < 0) {
      c.consumo = 0;
    }
  }
}

List<Coche> coches = [
    Coche('Toyota', 'Corolla', 2018, 1300, 120, false, 4, 5, 6.0, 50.0),
    Coche('Tesla', 'Model 3', 2022, 1700, 283, true, 4, 5, 0.0, 75.0),
    Coche('Seat', 'Ibiza', 2016, 1150, 95, false, 3, 5, 5.5, 45.0),
    Coche('Volkswagen', 'Golf', 2020, 1400, 150, true, 5, 5, 6.2, 50.0),
    Coche('BMW', '320i', 2019, 1550, 184, true, 4, 5, 7.1, 60.0),
    Coche('Audi', 'A3', 2021, 1450, 150, true, 5, 5, 5.8, 50.0),
    Coche('Renault', 'Clio', 2017, 1100, 90, false, 5, 5, 5.3, 45.0),
    Coche('Fiat', 'Panda', 2015, 950, 70, false, 3, 4, 5.0, 35.0),
    Coche('Ford', 'Focus', 2020, 1350, 125, true, 5, 5, 6.4, 52.0),
    Coche('Hyundai', 'i30', 2021, 1300, 120, false, 5, 5, 6.0, 48.0),
];

void main(){
  print('Coches automáticos: ');
  List<Coche> automaticos = soloAutomaticos(coches);
  automaticos.forEach(print);

  print('\nCoches posteriores a 2019: ');
  List<Coche> recientes = posterioresA(coches, 2019);
  recientes.forEach(print);

  print('\nTop 3 coches autonomía');
  List<Coche> top3 = topAutonomia(coches, 3);
  top3.forEach((c) {
    print('${c.marca} ${c.modelo} -> ${c.autonomia().toStringAsFixed(2)} km');
  });

  double mediaSeat = potenciaMediaMarca(coches, 'Seat');
  print('\nPotencia media Seat: ${mediaSeat.toStringAsFixed(2)}');

  print('\nReduciendo consumo un 10%');
  reducirConsumo(coches, 10);
  coches.forEach((c) {
    print('${c.marca} ${c.modelo} -> consumo: ${c.consumo}');
  });
}

