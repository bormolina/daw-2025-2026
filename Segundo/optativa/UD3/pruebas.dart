import 'models/Persona.dart';
import 'models/Coche.dart';

void main() {
  Persona p1 = Persona('Ana', 30);
  Persona p2 = Persona('Luis', 25);

  print(p1);
  p1.saludar();
  print(p2);
  p2.saludar();


  Coche c = Coche("Toyoto", "Corollo", 2252, 1520, 120, false, 2, 4, 5, 50);
  print(c);
}