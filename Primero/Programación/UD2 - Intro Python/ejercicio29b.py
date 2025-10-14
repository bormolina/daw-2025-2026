nombreUsuario = input("Introduce tu nombre de usuario: ")

while True:
    pass1 = input("Introduce tu contraseña: ")
    pass2 = input("Introduce de nuevo tu contraseña: ")
    if pass1 == pass2:
        break
    else:
        print("Las contraseñas no coinciden")

print("Usuario creado correctamente")