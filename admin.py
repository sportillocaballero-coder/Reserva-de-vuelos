from vuelos import agregarVuelo, vuelos

def modoAdmin():
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