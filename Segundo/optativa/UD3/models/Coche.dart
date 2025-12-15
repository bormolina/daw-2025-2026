class Coche {
  String marca;
  String modelo;
  int anio_fabricacion;
  int peso;
  int potencia;
  bool automatico;
  int num_puertas;
  int num_asientos;
  double consumo;
  double deposito;

  Coche(this.marca, this.modelo, this.anio_fabricacion, this.peso, this.potencia, this.automatico, this.num_puertas, this.num_asientos, this.consumo, this.deposito);

  double autonomia(){
    if(this.consumo == 0){
      return -1; // Indica que es un coche eléctrico
    }
    else{
      return this.deposito / this.consumo * 100;
    }
    
  }

  @override
  String toString(){
    return 'Coche(marca: $marca, modelo: $modelo, año: $anio_fabricacion, peso: $peso, potencia: $potencia, automatico: $automatico, num_puertas: $num_puertas, num_asientos: $num_asientos, consumo: $consumo, deposito: $deposito)';
  }

}