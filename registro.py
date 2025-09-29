import random
# La lista paralelas, aca se guardan el usuario y contraseña de los clientes por posicion 
usuarios = []
contraseñas = []
vuelos = []
reservas = []

#Se registran los clientes
def registrarUsuario():
    """
    Objetivo: Registrar un nuevo usuario y contraseña si el usuario no existe.
    Parámetros: Ninguno (usa input).
    Retorna: Nada.
    """ 
    print("\n--Registro--")
    nuevo_usuario = input("Ingrese un nombre de usuario: ").strip()

    if nuevo_usuario in usuarios:
        print("Ese usuario ya esta registrado\n")
    else:
        nueva_contraseña = input("Ingrese una contraseña: ").strip()
        usuarios.append(nuevo_usuario)
        contraseñas.append(nueva_contraseña)
        print("Registro exitoso\n")

# Login de clientes
def Login():
    """
    Objetivo: Permitir que un usuario registrado inicie sesión.
    Parámetros: Ninguno (usa input).
    Retorna:
      - str: Nombre de usuario si el login es exitoso.
      - None: Si falla el login.
    """
    print("\n--- Iniciar Sesión ---")
    usuario = input("Usuario: ")
    contraseña = input("Contraseña: ")

    if usuario in usuarios:
        i = usuarios.index(usuario)
        if contraseñas[i] == contraseña:
            print(f"Bienvenido/a, {usuario}\n")
            return usuario
        else:
            print("Contraseña incorrecta\n")
    else:
        print("El usuario no existe\n")

    return None

# Interfaz, en donde el programa se ejecuta 
def main():
    """
    Objetivo: Menu principal para registrar, iniciar sesion o salir
    Parametros: Ninguno
    Retorna: Nada
    """
    opcion = "0"
    while True:  
        print("===VUELOS====")
        print("1. Registrarse")
        print("2. Iniciar sesion")
        print("3. Salir")
        print("4. Agregar Vuelo")
        print("5. Eliminar Vuelo")
        print("6. Reservar Vuelo")
        print("7. Ver Reservas")
        print("8. Buscar Vuelos")  
        print("9. Mostrar vuelos")
        opcion = input("Elegi una opcion: ")

        if opcion == "1":
            registrarUsuario()
        elif opcion == "2":
            usuario_logueado = Login()
            if usuario_logueado is not None:
                print(f" Usuario logueado: {usuario_logueado}")
            
        elif opcion == "3":
            print(" ¡Hasta luego!\n")
        else:
            print("Opcion invalida. \n")

if __name__ == "__main__":
    main()