from vuelos import agregarVuelo, eliminarVuelo, busquedaVuelos, modificarVuelo
from estadistica import estadisticas
from reservas import historialReservas

def modoAdmin():
    """
    Objetivo: Permitir acceso al panel de administracion del sistema.
    Parametros: Ninguno.
    Retorna: Nada.
    """
    print("\n-- Administracion --")

    user = input("Usuario del Admin: ").strip()
    while not user:
        print("ERROR: el usuario no puede estar vacio")
        user = input("Usuario del Admin: ").strip()
    
    password = input("Contrasena: ").strip()
    while not password:
        print("ERROR: la contrasena no puede estar vacia")
        password = input("Contrasena: ").strip()
    
    if user == "admin" and password == "1234":
        print("Acceso admitido")

        opcion = "0"
        while opcion != "5":
            print("\n=== MENU ADMIN ===")
            print("1. Agregar un vuelo al sistema")
            print("2. Mostrar vuelos")
            print("3. Estadisticas")
            print("4. Historial de Reservas")
            print("5. Salir")

            opcion = input("Seleccione una opcion: ").strip()

            if opcion == "1":
                menuVuelos()
            elif opcion == "2":
                busquedaVuelos()
            elif opcion == "3":
                estadisticas()
            elif opcion == "4":
                historialReservas()
            elif opcion == "5":
                print("Saliendo de Admin")            
            else:
                print("Opcion invalida")
    else:
        print("Credenciales invalidas")
    

def menuVuelos():
    """
    Submenú para gestionar vuelos.
    """
    opcion = "0"
    while opcion != "5":
        print("\n--- Gestión de Vuelos ---")
        print("1. Agregar vuelo")
        print("2. Modificar vuelo")
        print("3. Eliminar vuelo")
        print("4. Buscar/Listar vuelos")
        print("5. Volver al menú principal")
        opcion = input("Seleccione una opción: ").strip()
        
        if opcion == "1":
            agregarVuelo()
        elif opcion == "2":
            modificarVuelo()
        elif opcion == "3":
            eliminarVuelo()
        elif opcion == "4":
            busquedaVuelos()
        elif opcion == "5":
            print("Volviendo al menú principal...")
        else:
            print("Opción inválida")