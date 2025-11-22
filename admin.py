from vuelos import agregarVuelo, eliminarVuelo,busquedaVuelos
from estadistica import estadisticas

def modoAdmin():
    """
    Objetivo: Permitir acceso al panel de administracion del sistema.
    Parametros: Ninguno.
    Retorna: Nada.
    """
    print("\n-- Administracion --")

    
    user = input("Usuario del Admin: ").strip()
    password = input("Contrasena: ").strip()

    
    if user == "admin" and password == "1234":
        print("Acceso admitido")

        opcion = "0"
        while opcion != "4":
            print("\n=== MENU ADMIN ===")
            print("1. Agregar un vuelo al sistema")
            print("2. Mostrar vuelos")
            print("3. Estadisticas")
            print("4. Salir")

            opcion = input("Seleccione una opcion: ").strip()

            if opcion == "1":
                menuVuelos()
            elif opcion == "2":
                busquedaVuelos()
            elif opcion == "3":
                estadisticas()
            elif opcion == "4":
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
    while opcion != "4":
        print("\n--- Gestión de Vuelos ---")
        print("1. Agregar vuelo")
        print("2. Eliminar vuelo")
        print("3. Buscar/Listar vuelos")
        print("4. Volver al menú principal")
        opcion = input("Seleccione una opción: ").strip()
        
        if opcion == "1":
            agregarVuelo()
        elif opcion == "2":
            eliminarVuelo()
        elif opcion == "3":
            busquedaVuelos()
        elif opcion == "4":
            print("Volviendo al menú principal...")
        else:
            print("Opción inválida")

#TODO: opciones del admin:
#- Gestionar vuelos (agregar, eliminar, listar, editar) 
#_______ Falta funcion de modificar vuelos 
#- Gestionar usuarios (listar, eliminar, resetear contrasena)
