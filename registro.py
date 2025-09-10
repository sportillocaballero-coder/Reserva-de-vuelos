# La lista paralelas, aca se guardan el usuario y contraseña de los clientes por posicion 
usuarios = []
contraseñas = []

#Se registran los clientes
def RegistrarUsuario():
    print("\n--Registro--")
    nuevo_usuario = input("Ingrese un nombre de usuario: ")

    if nuevo_usuario in usuarios:
        print("Ese usuario ya está registrado.\n")
    else:
        nueva_contraseña = input("Ingrese una contraseña: ")
        usuarios.append(nuevo_usuario)
        contraseñas.append(nueva_contraseña)
        print("✅ Registro exitoso.\n")

# Login de clientes
def Login():
    print("\n--- Iniciar Sesión ---")
    usuario = input("Usuario: ")
    contraseña = input("Contraseña: ")

    if usuario in usuarios:
        i = usuarios.index(usuario)
        if contraseñas[i] == contraseña:
            print(f"✅ Bienvenido/a, {usuario}.\n")
            return usuario
        else:
            print("Contraseña incorrecta.\n")
    else:
        print("El usuario no existe.\n")

    return None

# Interfaz, en donde el programa se ejecuta 
def main():
    opcion = "0"
    while opcion != "3":
        print("===VUELOS====")
        print("1. Registrarse")
        print("2. Iniciar sesión")
        print("3. Salir")
        opcion = input("Elegí una opción: ")

        if opcion == "1":
            RegistrarUsuario()
        elif opcion == "2":
            usuario_logueado = Login()
            if usuario_logueado is not None:
                print(f" Usuario logueado: {usuario_logueado}")
                # Aca es donde se podrian llamar las funciones de reserva, busqueda, etc...
        elif opcion == "3":
            print(" ¡Bai bai!\n")
        else:
            print("Opcion invalida. \n")

if __name__ == "__main__":
    main()