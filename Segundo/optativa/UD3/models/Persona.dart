class Persona {
  String nombre;
  int edad;

  // Constructor
  Persona(this.nombre, this.edad);

  // Método
  void saludar() {
    print('Hola, me llamo $nombre y tengo $edad años.');
  }
  
  @override
  String toString() {
    return 'Persona(nombre: $nombre, edad: $edad)';
  }
}

