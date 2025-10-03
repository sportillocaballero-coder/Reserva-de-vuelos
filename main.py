from usuarios import registrarUsuario, login
from vuelos import agregarVuelo, eliminarVuelo, busquedaVuelos, vuelos
from reservas import reservarVuelo, verReserva
from admin import modoAdmin

hola = int(input("Saluda:"))
def menuVuelos(usuario):
#TODO: mostrar tambien historial de reservas
#TODO: permitir cancelar una reserva
#TODO: permitir pagar una reserva
#TODO: En todo caso de que el codigo quede muy desordenado, podemos hacer un menu jerarquico
    """
    Objetivo: Mostrar el menu de opciones disponibles para usuarios logueados.
    Parametros:
      - usuario (str): Usuario logueado.
    Retorna: Nada.
    """
    opcion = "0"
    while opcion != "4":
        print(f"\n=== BIENVENIDO ({usuario}) ===")
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

if __name__ == "__main__":
    menuPrincipal()

#TODO: #TODO: AVANZADO: Crear persistencias de datos con JSON en el que cada variable print tenga un idioma como portugues, ingles y español, el usuario tendra la oportunidad de elejir su idioma
