from Libro import Libro
from Biblioteca import Biblioteca

# Crear libros
l1 = Libro(
    "978-84-376-0494-7",
    "El Quijote",
    ["Miguel de Cervantes"],
    ["Novela"],
    380000,
    20.00
)

l2 = Libro(
    "978-84-670-5941-8",
    "Cien años de soledad",
    ["Gabriel García Márquez"],
    ["Novela"],
    144000,
    18.50
)

l3 = Libro(
    "978-84-233-5396-5",
    "La sombra del viento",
    ["Carlos Ruiz Zafón"],
    ["Misterio", "Novela"],
    165000,
    15.00
)

l4 = Libro(
    "978-84-339-0154-2",
    "Ficciones",
    ["Jorge Luis Borges"],
    ["Relatos"],
    75000,
    12.00
)

# Crear biblioteca con lista inicial de libros
biblioteca = Biblioteca(
    id_biblioteca = 1,
    nombre = "Biblioteca Municipal",
    direccion = "Calle Real 12, Monachil",
    libros = [l1, l2, l3]
)

print("=== Biblioteca inicial ===")
print(biblioteca)
print()

print("=== Añadir libro ===")
# biblioteca.libros.append(l4) --> MAL!!! GOLPE DE REMO. TE SALTAS ENCAPSULACIÓN
biblioteca.añadir_libro(l4)
print(biblioteca)
print()

print("=== Contar libros ===")
print(biblioteca.contar_libros())
print()

print("=== Buscar libros por palabra ===")
resultado = biblioteca.buscar_libros_por_palabra("viento")
for libro in resultado:
    print(libro.titulo)
print()

print("=== Buscar libros por autor ===")
resultado = biblioteca.buscar_libros_por_autor("Gabriel García Márquez")
for libro in resultado:
    print(libro.titulo)
print()

print("=== Buscar libros por precio máximo ===")
resultado = biblioteca.buscar_libros_por_precio_maximo(15.00)
for libro in resultado:
    print(f"{libro.titulo} - {libro.precio_venta} €")
print()

print("=== Libro más largo (por operadores) ===")
libro = biblioteca.libro_mas_largo()
print(libro.titulo if libro else "No hay libros")
print()

print("=== Libro más corto (por operadores) ===")
libro = biblioteca.libro_mas_corto()
print(libro.titulo if libro else "No hay libros")
print()

print("=== Libros ordenados por longitud ===")
for libro in biblioteca.libros_ordenados_por_longitud():
    print(f"{libro.titulo} ({libro.n_palabras} palabras)")
print()

print("=== Libro más caro ===")
libro = biblioteca.libro_mas_caro()
print(libro.titulo if libro else "No hay libros")
print()

print("=== Libro más barato ===")
libro = biblioteca.libro_mas_barato()
print(libro.titulo if libro else "No hay libros")
print()

print("=== Libros ordenados por precio ===")
for libro in biblioteca.libros_ordenados_por_precio():
    print(f"{libro.titulo} - {libro.precio_venta} €")
print()
