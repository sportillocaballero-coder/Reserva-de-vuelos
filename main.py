from usuarios import registrarUsuario, login, cambiarContrasena, editarPerfil, cambiarNombreUsuario
from vuelos import busquedaVuelos
from reservas import reservarVuelo, verReserva, cancelarReserva
from admin import modoAdmin


def menuPrincipal():
    """
    Objetivo: Mostrar el menu principal del sistema de reservas.
    Parametros: Ninguno.
    Retorna: Nada.
    """
    opcion = "0"
    while opcion != "4":
        print("\n=== MENU PRINCIPAL ===")
        print("1. Registrate")
        print("2. Login")
        print("3. Modo Admin")
        print("4. Salir")

        opcion = input("Seleccione una opcion: ").strip()
        if opcion == "1":
            registrarUsuario()
        elif opcion == "2":
            usuario = login()
            if usuario is not None:
                menuVuelos(usuario) 
        elif opcion == "3":
            modoAdmin()
        elif opcion == "4":
            print("Nos vemos!")
        else:
            print("Opcion invalida")


def menuVuelos(usuario):
    """
    Submenú de usuario tras login: buscar vuelos, reservar, ver reservas, cerrar sesión.
    """
    opcion = "0"
    while opcion != "6":
        print(f"\n--- Menu de {usuario} ---")
        print("1. Buscar/Listar vuelos")
        print("2. Reservar vuelo")
        print("3. Ver mis reservas")
        print("4. Cancelar reserva")
        print("5. Editar perfil")
        print("6. Cerrar sesión")
        opcion = input("Seleccione una opción: ").strip()

        if opcion == "1":
            busquedaVuelos()
        elif opcion == "2":
            reservarVuelo(usuario)
        elif opcion == "3":
            verReserva(usuario)
        elif opcion == "4":
            cancelarReserva(usuario)
        elif opcion == "5":
            usuario = editarPefilMenu(usuario)
            if usuario is None:
                print("Cerrando sesión...")
                break
        elif opcion == "6":
            print("Cerrando sesión...")
        else:
            print("Opción inválida")

def editarPefilMenu(usuario):
    """
    Menu para editar perfil de usuario"""
    opcion = "0"
    while opcion != "4":
        print(f"\n---- Editor de perfil {usuario} ----")
        print("1. Cambiar contraseña")
        print("2. Cambiar nombre de usuario")
        print("3. Editar perfil completo")
        print("4. Volver")
        opcion = input("Seleccione una opción: ").strip()

        if opcion == "1":
            cambiarContrasena(usuario)
        elif opcion == "2":
            nuevo_usuario = cambiarNombreUsuario(usuario)
            if nuevo_usuario:
                usuario = nuevo_usuario
        elif opcion == "3":
            nuevo_usuario = editarPerfil(usuario)
            if nuevo_usuario:
                usuario = nuevo_usuario
        elif opcion == "4":
            print("Volviendo al menú anterior...")
        else:
            print("Opción inválida")
    
    return usuario

if __name__ == "__main__":
    menuPrincipal()


