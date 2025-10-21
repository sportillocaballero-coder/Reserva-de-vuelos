from usuarios import registrarUsuario, login
from vuelos import agregarVuelo, eliminarVuelo, busquedaVuelos, vuelos
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
    while opcion != "5":
        print("\n=== MENU PRINCIPAL ===")
        print("1. Registrate")
        print("2. Login")
        print("3. Modo Admin")
        print("4. Pagar reserva")
        print("5. Salir")

        opcion = input("Seleccione una opcion: ").strip()
        if opcion == "1":
            registrarUsuario()
        elif opcion == "2":
            usuario = login()
            if usuario is not None:
                menuVuelos(usuario) # type: ignore
        elif opcion == "3":
            modoAdmin()
        elif opcion == "4": #NUEVO###
            id_reserva = input("Ingrese el ID de la reserva a pagar: ")
            reservas[:] = pagar_reserva(reservas, id_reserva) # type: ignore
            print("✅ Reserva pagada correctamente (si estaba pendiente).")
        elif opcion == "5":
            print("Nos vemos!")
        else:
            print("Opcion invalida")

if __name__ == "__main__":
    menuPrincipal()

#TODO: #TODO: AVANZADO: Crear persistencias de datos con JSON en el que cada variable print tenga un idioma como portugues, ingles y español, el usuario tendra la oportunidad de elejir su idioma
