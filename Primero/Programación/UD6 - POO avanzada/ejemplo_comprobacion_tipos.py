# Clase base
class A:
    pass


# Clase B hereda de A
class B(A):
    pass


# Clase C hereda de B
class C(B):
    pass


# Creamos un objeto de la clase C
obj = C()


# ------------------------------
# isinstance()
# ------------------------------

# Comprueba si obj es instancia de C
print(isinstance(obj, C))  # True

# Comprueba si obj es instancia de B
# También devuelve True porque C hereda de B
print(isinstance(obj, B))  # True

# Comprueba si obj es instancia de A
# También True porque C -> B -> A
print(isinstance(obj, A))  # True

# Todas las clases heredan de object
print(isinstance(obj, object))  # True


# ------------------------------
# issubclass()
# ------------------------------

# Comprueba si B hereda de A
print(issubclass(B, A))  # True

# Comprueba si C hereda de A (indirectamente)
print(issubclass(C, A))  # True

# Comprueba si A hereda de B
print(issubclass(A, B))  # False

# Todas las clases heredan de object
print(issubclass(A, object))  # True
print(issubclass(B, object))  # True
print(issubclass(C, object))  # True