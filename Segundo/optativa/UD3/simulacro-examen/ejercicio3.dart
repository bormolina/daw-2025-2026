import 'Videojuego.dart';
import 'Steam.dart';

void main() {
  // Crear videojuegos
  Videojuego v1 = Videojuego('The Last of Us', 80.5, ['Acción', 'Aventura'], 18);
  Videojuego v2 = Videojuego('FIFA 24', 45.0, ['Deportes'], 3);
  Videojuego v3 = Videojuego('Minecraft', 1.2, ['Aventura', 'Sandbox'], 7);
  Videojuego v4 = Videojuego('Dark Souls', 25.0, ['Acción', 'RPG'], 16);
  Videojuego v5 = Videojuego('Stardew Valley', 0.8, ['Simulación', 'Indie'], 7);

  // Lista de videojuegos
  List<Videojuego> biblioteca = [v1, v2, v3, v4, v5];

  // Crear Steam con la biblioteca
  Steam steam = Steam(biblioteca);

  // Obtener juegos de un género
  List<Videojuego> juegosAccion = steam.juegosPorGenero('Acción');

  // Mostrar resultados
  for (Videojuego juego in juegosAccion) {
    print(juego);
  }
}