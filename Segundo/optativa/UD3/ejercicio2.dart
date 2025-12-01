int maximo(List<int> l){
  int n_max = l[0];
  for(int n in l){
    if(n > n_max){
      n_max = n;
    } 
  }
  return n_max;
}

int minimo(List<int> l){
  int n_min = l[0];
  for(int n in l){
    if(n < n_min){
      n_min = n;
    } 
  }
  return n_min;
}

double media(List<int> l){
  int sumatoria = 0;
  for(int n in l){
    sumatoria += n;
  }
  return sumatoria / l.length;
}


void main(){
  List<int> numeros = [
    3, 10, 1, 7, 0, 4, 9, 2, 6, 8,
    5, 3, 10, 1, 7, 0, 4, 9, 2, 6
  ];

  int n_max = maximo(numeros);
  int n_min = minimo(numeros);
  double n_media = media(numeros);
  print('El máximo es: $n_max');
  print('El mínimo es: $n_min');
  print('La media es $n_media');
}

