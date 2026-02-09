from Libro import Libro

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
    "978-84-204-8493-9",
    "El Quijote (edición bolsillo)",
    ["Miguel de Cervantes"],
    ["Novela"],
    380000,
    10.00
)

print("=== Mostrar libros ===")
print(l1)
print()
print(l2)
print()

print("=== Comparación por igualdad (ISBN) ===")
print(l1 == l3)   # True (mismo ISBN)
print(l1 == l2)   # False
print()

print("=== Comparaciones relacionales (n_palabras) ===")
print(l1 > l2)
print(l2 < l1)
print(l2 <= l1)
print(l1 >= l3)
print()

print("=== Longitud del libro (len) ===")
print(len(l1))
print(len(l2))
print()

print("=== Contención de palabras en el título ===")
print("Quijote" in l1)
print("soledad" in l2)
print("Python" in l1)
print()

print("=== Clasificación por longitud ===")
print(l1.longitud())
print(l2.longitud())
print()

print("=== Aplicar descuento ===")
print(f"Precio antes: {l1.precio_venta} €")
l1.aplicar_descuento(0.10)
print(f"Precio después: {l1.precio_venta} €")
print()

print("=== Ordenar libros con sorted() ===")
libros = [l1, l2, l3]
libros_ordenados = sorted(libros, reverse=True)
for libro in libros_ordenados:
    print(f"{libro.titulo} ({libro.n_palabras} palabras)")
