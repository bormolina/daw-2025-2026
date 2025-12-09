void main() {
  // Listas originales (con repetidos)
  List<String> juegosJavier = [
    "Dark Souls",
    "Hollow Knight",
    "Celeste",
    "Celeste",
    "Elden Ring",
    "Hades"
  ];

  List<String> juegosMarta = [
    "Hollow Knight",
    "Stardew Valley",
    "Hades",
    "Hades",
    "Terraria"
  ];

  // Convertimos las listas a conjuntos
  Set<String> setJavier = juegosJavier.toSet();
  Set<String> setMarta = juegosMarta.toSet();

  // a) Juegos que tienen ambos (intersección)
  List<String> ambos = setJavier.intersection(setMarta).toList();
  print("a) Juegos que tienen ambos: $ambos");

  // b) Juegos que tiene Javier pero no Marta
  List<String> soloJavier = setJavier.difference(setMarta).toList();
  print("b) Juegos que tiene Javier pero no Marta: $soloJavier");

  // c) Juegos que tiene Marta pero no Javier
  List<String> soloMarta = setMarta.difference(setJavier).toList();
  print("c) Juegos que tiene Marta pero no Javier: $soloMarta");

  // d) ¿Javier tiene repetidos?
  bool repetidosJavier = juegosJavier.length != setJavier.length;
  print("d) ¿Javier tiene repetidos? $repetidosJavier");

  // e) ¿Marta tiene repetidos?
  bool repetidosMarta = juegosMarta.length != setMarta.length;
  print("e) ¿Marta tiene repetidos? $repetidosMarta");

  // f) Biblioteca conjunta (unión)
  List<String> bibliotecaConjunta = setJavier.union(setMarta).toList();
  print("f) Biblioteca conjunta: $bibliotecaConjunta");
}