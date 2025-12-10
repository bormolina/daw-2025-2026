import 'dart:io';
import 'models/Coche.dart';

void main(){
  print("Dame el marca: ");
  String marca = stdin.readLineSync() ?? '';
  print("Dame el módelo: ");
  String modelo = stdin.readLineSync() ?? '';
  print("Dame el año de fabricación: ");
  int ano = int.parse(stdin.readLineSync() ?? '0');
  print("Dame el peso: ");
  int peso = int.parse(stdin.readLineSync() ?? '0');
  print("Dame la potencia: ");
  int potencia = int.parse(stdin.readLineSync() ?? '0');
  print("Es automático: (S/N)");
  bool automatico = true;
  String es_automatico = stdin.readLineSync() ?? 'N';
  while(es_automatico != 'S' && es_automatico != 'N'){
    print("Es automático: (S/N)");
    String es_automatico = stdin.readLineSync() ?? 'N';
  }

  if(es_automatico == 'N'){
    automatico = false;
  }
  
  print('Número de puertas: ');
  int num_puertas = int.parse(stdin.readLineSync() ?? '0');

  print('Número de asientos: ');
  int num_asientos = int.parse(stdin.readLineSync() ?? '0');

  print('Consumo: ');
  double consumo = double.parse(stdin.readLineSync() ?? '0');

  print('Depósito: ');
  double deposito = double.parse(stdin.readLineSync() ?? '0');

  Coche c = Coche(marca, modelo, ano, peso, potencia, automatico, num_puertas, num_asientos, consumo, deposito);

  print(c);

}