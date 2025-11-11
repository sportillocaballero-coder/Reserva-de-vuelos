from usuarios import registrarUsuario, login
from vuelos import busquedaVuelos
from reservas import reservarVuelo, verReserva
from admin import modoAdmin


def menuPrincipal():
#TODO: #TODO cargar datos de usuarios con JSON
#TODO: #TODO guardar datos en JSON al salir
#TODO: agregar opcion para ver estadisticas basicas desde el menu principal
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
    while opcion != "4":
        print(f"\n--- Menu de {usuario} ---")
        print("1. Buscar/Listar vuelos")
        print("2. Reservar vuelo")
        print("3. Ver mis reservas")
        print("4. Cerrar sesión")
        opcion = input("Seleccione una opción: ").strip()

        if opcion == "1":
            busquedaVuelos()
        elif opcion == "2":
            reservarVuelo(usuario)
        elif opcion == "3":
            verReserva(usuario)
        elif opcion == "4":
            print("Cerrando sesión...")
        else:
            print("Opción inválida")

if __name__ == "__main__":
    menuPrincipal()

#TODO: #TODO: AVANZADO: Crear persistencias de datos con JSON en el que cada variable print tenga un idioma como portugues, ingles y español, el usuario tendra la oportunidad de elejir su idioma
