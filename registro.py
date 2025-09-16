# La lista paralelas, aca se guardan el usuario y contraseña de los clientes por posicion 
usuarios = []
contraseñas = []
idVuelos =[12345,54321,53421]
origenes = ["Argentina","Peru","Uruguay"]
destinos = ["Paraguay","Chile","Brasil"]

#Se registran los clientes
def RegistrarUsuario():
    """
    Objetivo: Registrar un nuevo usuario y contraseña si el usuario no existe
    Parametros: Ninguno (usa input)
    Retorna: Nada
    """
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
    """
    Objetivo: Permitir que un usuario registrado inicie sesion
    Parametros: Ninguno (usa input)
    Retorna:
      - str: Nombre de usuario si el login es exitoso
      - None: Si falla el login
    """
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

def busquedaVuelos():
    print("\n--- Elige el origen del vuelo ---")
    c = 0
    for origen in origenes:
        print(f"{c + 1} -El origen del vuelo es: {origen}")
        print(f"El destino del vuelo es: {destinos[c]}\n")
        c += 1
    seleccionVuelo = int(input(f"Seleccione el vuelo por su numero 1 a {len(origenes)}: "))
    while seleccionVuelo > len(origenes) or seleccionVuelo < 1:
        print("Error en la seleccion del vuelo")
        seleccionVuelo = int(input(f"Seleccione el vuelo por su numero 1 a {len(origenes)}: "))
    print(f"Usted ah seleccionado el vuelo con origen {origenes[seleccionVuelo-1]} y destino {destinos[seleccionVuelo - 1]}\n")

# Interfaz, en donde el programa se ejecuta 
def main():
    """
    Objetivo: Menu principal para registrar, iniciar sesion o salir
    Parametros: Ninguno
    Retorna: Nada
    """
    opcion = "0"
    while opcion != "3":
        print("===VUELOS====")
        print("1. Registrarse")
        print("2. Iniciar sesión")
        print("3. Salir")
        print("4. Buscar Vuelos")
        opcion = input("Elegí una opción: ")

        if opcion == "1":
            RegistrarUsuario()
        elif opcion == "2":
            usuario_logueado = Login()
            if usuario_logueado is not None:
                print(f" Usuario logueado: {usuario_logueado}")
                # Aca es donde se podrian llamar las funciones de reserva, busqueda, etc...
        elif opcion == "3":
            print(" ¡Hasta luego!\n")
        elif opcion == "4":
            busquedaVuelos()
        else:
            print("Opcion invalida. \n")

if __name__ == "__main__":
    main()