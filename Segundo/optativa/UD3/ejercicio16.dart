void main() {
  List<String> cancionesAna = [
    "Master of Puppets",
    "Painkiller",
    "Hallowed Be Thy Name",
    "Hallowed Be Thy Name",
    "Holy Wars",
    "Chop Suey!"
  ];

  List<String> cancionesLuis = [
    "Painkiller",
    "Holy Wars",
    "Chop Suey!",
    "Walk",
    "Walk",
    "The Trooper"
  ];

  Set<String> anaSinRepetidos = cancionesAna.toSet();
  Set<String> luisSinRepetidos = cancionesLuis.toSet();

  print('Ana sin repetidos: $anaSinRepetidos');
  print('Luis sin repetidos: $luisSinRepetidos');

  // Canciones que tienen ambos usuarios
  Set<String> comunes = anaSinRepetidos.intersection(luisSinRepetidos);
  print('\nCanciones en común: $comunes');

  //Canciones que tiene Ana pero no Luis
  Set<String> soloAna = anaSinRepetidos.difference(luisSinRepetidos);
  print('\nCanciones solo de Ana: $soloAna');

  // Indicar si alguno tiene canciones repetidas
  bool anaTieneRepetidos = cancionesAna.length != anaSinRepetidos.length;
  bool luisTieneRepetidos = cancionesLuis.length != luisSinRepetidos.length;

  print('\n¿Ana tiene canciones repetidas? $anaTieneRepetidos');
  print('¿Luis tiene canciones repetidas? $luisTieneRepetidos');

  // Playlist conjunta (sin repetidos)
  Set<String> playlistConjunta = anaSinRepetidos.union(luisSinRepetidos);
  print('\nPlaylist conjunta: $playlistConjunta');

  // Canciones que tiene Luis pero no Ana
  Set<String> soloLuis = luisSinRepetidos.difference(anaSinRepetidos);
  print('\nCanciones solo de Luis: $soloLuis');
}