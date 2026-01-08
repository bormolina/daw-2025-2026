class Producto {
  String nombre;
  double precio;
  List<String> categoria;

  Producto(this.nombre, this.precio, this.categoria);

  // Constructor desde JSON
  factory Producto.fromJson(Map<String, dynamic> json) {
    return Producto(
      json['nombre'],
      json['precio'],
      List<String>.from(json['categoria']),
    );
  }

  @override
  String toString() {
    return 'Producto: $nombre, Precio: $precio €, Categorías: ${categoria.join(', ')}';
  }
}