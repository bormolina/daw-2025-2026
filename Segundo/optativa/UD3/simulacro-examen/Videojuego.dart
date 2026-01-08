class Videojuego {
  String nombre;
  double peso;
  List<String> generos;
  int pegi;

  // Constructor
  Videojuego(this.nombre, this.peso, this.generos, this.pegi);

  // Método toString
  @override
  String toString() {
    return 'Videojuego: $nombre, Peso: $peso GB, Géneros: ${generos.join(', ')}, PEGI: $pegi';
  }

  // Método mayorEdad
  bool mayorEdad() {
    return pegi >= 18;
  }
}