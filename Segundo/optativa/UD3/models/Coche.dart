class Coche {
  String marca;
  String modelo;
  int ano_fabricacion;
  int peso;
  int potencia;
  bool automatico;
  int num_puertas;
  int num_asientos;
  double consumo;
  double deposito;

  Coche(this.marca, this.modelo, this.ano_fabricacion, this.peso, this.potencia, this.automatico, this.num_puertas, this.num_asientos, this.consumo, this.deposito);

  double autonomia(){
    return this.deposito / this.consumo * 100;
  }

  @override
  String toString(){
    return 'Coche(marca: $marca, modelo: $modelo, ...)';
  }

}