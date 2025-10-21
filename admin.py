<<<<<<< HEAD
from vuelos import agregarVuelo, vuelos
from estadistica import estadisticas
=======
from vuelos import agregarVuelo, eliminarVuelo, busquedaVuelos, vuelos
import estadistica
>>>>>>> 5175835b230e601b324e1a4ebc7a2cef54642bd8

def modoAdmin():
# TODO: importar funciones de estadisticas
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
    # Admins válidos
    # admins = [{"user": "admin", "password": "1234"}]
    # acceso = False
    # for adm in admins:
    # if adm["user"] == user and adm["password"] == password:
    # acceso = True
    # break

    # if acceso:
    #print("Acceso admitido")
    
        opcion = "0"
        while opcion != "4":
            print("\n=== MENU ADMIN ===")
<<<<<<< HEAD
            print("1. Agregar un vuelo al sistema")
            print("2. Mostrar vuelos")
            print("3. Estadisticas")
            print("4. Salir")
=======
            print("1. Gestionar vuelos")
            print("2. Gestionar usuarios")
            print("3. Gestionar reservas")
            print("4. Ver estadísticas")
            print("5. Salir")
>>>>>>> 5175835b230e601b324e1a4ebc7a2cef54642bd8

            opcion = input("Seleccione una opcion: ").strip()

            if opcion == "1":
                menuVuelos()
            elif opcion == "2":
                print("(Módulo usuarios no implementado aún)")
            elif opcion == "3":
<<<<<<< HEAD
                estadisticas()
            elif opcion == "4":
                print("Saliendo de Admin")            
=======
                print("(Módulo reservas no implementado aún)")
            elif opcion == "4":
                if hasattr(estadistica, 'mostrar_estadisticas'):
                    estadistica.mostrar_estadisticas(vuelos)
                else:
                    print("No hay módulo de estadísticas disponible.")
            elif opcion == "5":
                    print("Saliendo de Admin...")
>>>>>>> 5175835b230e601b324e1a4ebc7a2cef54642bd8
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
#TODO: reemplazar contrasena fija por una lista de administradores, lo podriamos hacer con json tambien, pero tendriamos tantos archivos que habria qu ecrear carpetas para cada cosa, charlable
#TODO: permitir crear nuevos administradores por jerarquia
#TODO: mostrar menu interactivo con opciones de gestion

#TODO: opciones del admin:
#- Gestionar vuelos (agregar, eliminar, listar, editar)
#- Gestionar usuarios (listar, eliminar, resetear contrasena)
#- Gestionar reservas (ver todas, cancelar, confirmar pago)
#- Ver estadisticas (usuario mas activo, vuelo mas caro, etc.)