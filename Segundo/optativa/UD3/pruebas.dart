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

void main() {
  Persona p1 = Persona('Ana', 30);
  Persona p2 = Persona('Luis', 25);

  print(p1);
  p1.saludar();
  print(p2);
  p2.saludar();

}