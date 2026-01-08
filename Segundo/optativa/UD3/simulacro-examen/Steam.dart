import 'Videojuego.dart';

class Steam {
  
  List<Videojuego> biblioteca;

  Steam(this.biblioteca);

  // Añadir un nuevo videojuego a la biblioteca
  void addVideojuego(Videojuego videojuego) {
    biblioteca.add(videojuego);
  }

  // Dado un género, devuelve los videojuegos de ese género
  List<Videojuego> juegosPorGenero(String genero) {
    return biblioteca
        .where((juego) => juego.generos.contains(genero))
        .toList();
  }
}