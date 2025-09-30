from vuelos import agregarVuelo, vuelos

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

        opcion = "0"
        while opcion != "3":
            print("\n=== MENU ADMIN ===")
            print("1. Agregar un vuelo al sistema")
            print("2. Mostrar vuelos")
            print("3. Salir")

            opcion = input("Seleccione una opcion: ").strip()

            if opcion == "1":
                agregarVuelo()
            elif opcion == "2":
                print(vuelos)
            elif opcion == "3":
                print("Saliendo de Admin")
            else:
                print("Opcion invalida")
    else:
        print("Credenciales invalidas")
    
#TODO: reemplazar contrasena fija por una lista de administradores, lo podriamos hacer con json tambien, pero tendriamos tantos archivos que habria qu ecrear carpetas para cada cosa, charlable
#TODO: permitir crear nuevos administradores por gerarquia
#TODO: mostrar menu interactivo con opciones de gestion

#TODO: opciones del admin:
#- Gestionar vuelos (agregar, eliminar, listar, editar)
#- Gestionar usuarios (listar, eliminar, resetear contrasena)
#- Gestionar reservas (ver todas, cancelar, confirmar pago)
#- Ver estadisticas (usuario mas activo, vuelo mas caro, etc.)