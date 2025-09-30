from usuarios import registrarUsuario, login
from vuelos import agregarVuelo, eliminarVuelo, busquedaVuelos, vuelos
from reservas import reservarVuelo, verReserva
from admin import modoAdmin

def menuVuelos(usuario):
    opcion = "0"
    while opcion != "4":
        print(f"\n=== MENU DE VUELOS ({usuario}) ===")
        print("1. Reservar vuelo")
        print("2. Ver mis reservas")
        print("3. Buscar vuelos")
        print("4. Salir")

        opcion = input("Seleccione una opcion: ").strip()
        if opcion == "1":
            reservarVuelo(usuario)
        elif opcion == "2":
            verReserva(usuario)
        elif opcion == "3":
            busquedaVuelos()
        elif opcion == "4":
            print("Sesion cerrada")
        else:
            print("Opcion invalida")

def menuPrincipal():
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

if __name__ == "__main__":
    menuPrincipal()