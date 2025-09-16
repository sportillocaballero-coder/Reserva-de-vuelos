import random
# La lista paralelas, aca se guardan el usuario y contraseña de los clientes por posicion 
usuarios = []
contraseñas = []
vuelos = []
reservas = []

#Se registran los clientes
def RegistrarUsuario():
    """
    Objetivo: Registrar un nuevo usuario y contraseña si el usuario no existe.
    Parámetros: Ninguno (usa input).
    Retorna: Nada.
    """ 
    print("\n--Registro--")
    nuevo_usuario = input("Ingrese un nombre de usuario: ")

    if nuevo_usuario in usuarios:
        print("Ese usuario ya está registrado.\n")
    else:
        nueva_contraseña = input("Ingrese una contraseña: ")
        usuarios.append(nuevo_usuario)
        contraseñas.append(nueva_contraseña)
        print("✅ Registro exitoso.\n")

# Login de clientes
def Login():
    """
    Objetivo: Permitir que un usuario registrado inicie sesión.
    Parámetros: Ninguno (usa input).
    Retorna:
      - str: Nombre de usuario si el login es exitoso.
      - None: Si falla el login.
    """
    print("\n--- Iniciar Sesión ---")
    usuario = input("Usuario: ")
    contraseña = input("Contraseña: ")

    if usuario in usuarios:
        i = usuarios.index(usuario)
        if contraseñas[i] == contraseña:
            print(f"✅ Bienvenido/a, {usuario}.\n")
            return usuario
        else:
            print("Contraseña incorrecta.\n")
    else:
        print("El usuario no existe.\n")

    return None

def agregarVuelo():
    """
    Objetivo: Agregar un nuevo vuelo si el usuario está logueado y no existe un vuelo igual (origen, destino, fecha).
    Parámetros: Ninguno (usa input y variable global usuario).
    Retorna: Nada.
    """
    if not usuarios:
        print(" Tenés que iniciar sesión.")
        return
    origen = input("Origen: ")
    destino = input("Destino: ")
    fecha = input("Fecha (DD/MM/AAAA): ")
    precio = float(input("Precio: "))
    asientos = int(input("Asientos: "))

    vuelo = {
        "id": f"{random.randint(1000, 9999)}",
        "origen": origen,
        "destino": destino,
        "fecha": fecha,
        "precio": precio,
        "asientos": asientos
    }

    # evitar duplicados (mismo origen, destino y fecha)
    for v in vuelos:
        if v["origen"] == origen and v["destino"] == destino and v["fecha"] == fecha:
            print("Ese vuelo ya existe.")
            return

    vuelos.append(vuelo)
    print("Vuelo agregado con éxito.")

def reservar_vuelo(usuario):
    """
    Objetivo: Permitir a un usuario reservar asientos en un vuelo existente.
    Parámetros:
      - usuario (str): Usuario logueado.
    Retorna: Nada.
    """
    if not usuario:
        print("❌ Tenés que iniciar sesión.")
        return

    if not vuelos:
        print("No hay vuelos cargados.")
        return

    vid = input("ID del vuelo: ")
    cant = input("Cantidad de asientos: ")
    if not cant.isdigit():
        print("Cantidad invalida")
        return
    cant = int(cant)

    # buscar vuelo 
    vuelo = None
    for v in vuelos:
        if v["id"] == vid:
            vuelo = v
    if not vuelo:
        print("Vuelo no encontrado.")
        return
    if vuelo["asientos"] < cant:
        print(f"Solo hay {vuelo['asientos']} asientos.")
        return

    # actualizar vuelos
    vuelo["asientos"] -= cant

    # guardar nueva reserva en la lista
    reserva = {
        "id": f"R{len(reservas)+1:04d}",
        "usuario": usuario,
        "vuelo": vid,
        "cant": cant
    }
    reservas.append(reserva)

    print("✅ Reserva creada:", reserva)

def ver_reservas(usuario):
    """
    Objetivo: Mostrar todas las reservas realizadas por el usuario.
    Parámetros:
      - usuario (str): Usuario logueado.
    Retorna: Nada.
    """
    print("\n-- Reservas de", usuario, "--")
    tiene = False
    for r in reservas:
        if r["usuario"] == usuario:
            print(r)
            tiene = True
    if not tiene:
        print("No tenés reservas.")

def eliminar_vuelo():
    """
    Objetivo: Eliminar un vuelo existente por su ID.
    Parámetros: Ninguno (usa input).
    Retorna: Nada.
    """
    if not vuelos:
        print("No hay vuelos cargados.")
        return
    vid = input("ID del vuelo a eliminar: ")
    encontrado = False
    idx = None
    for i in range(len(vuelos)):
        if vuelos[i]["id"] == vid:
            idx = i
            encontrado = True
    if encontrado and idx is not None:
        del vuelos[idx]
        print("Vuelo eliminado con éxito.")
    else:
        print("Vuelo no encontrado.")

def busquedaVuelos():
    """
    Objetivo: Mostrar los vuelos disponibles y permitir seleccionar uno.
    Parámetros: Ninguno.
    Retorna: Nada.
    """
    if not vuelos:
        print("No hay vuelos cargados.")
        return
    print("\n--- Vuelos disponibles ---")
    for idx, vuelo in enumerate(vuelos, 1):
        print(f"{idx}. ID: {vuelo['id']} | Origen: {vuelo['origen']} | Destino: {vuelo['destino']} | Fecha: {vuelo['fecha']} | Precio: {vuelo['precio']} | Asientos: {vuelo['asientos']}")
    seleccion = input(f"Seleccione el vuelo por su número (1 a {len(vuelos)}), o presione Enter para salir: ")
    if seleccion.isdigit():
        seleccion = int(seleccion)
        if 1 <= seleccion <= len(vuelos):
            vuelo = vuelos[seleccion - 1]
            print(f"Usted ha seleccionado el vuelo con ID {vuelo['id']}, origen {vuelo['origen']} y destino {vuelo['destino']}\n")
        else:
            print("Selección inválida.")
    elif seleccion.strip() == "":
        print("Saliendo de la búsqueda de vuelos.")
    else:
        print("Selección inválida.")


# Interfaz, en donde el programa se ejecuta 
def main():
    """
    Objetivo: Menu principal para registrar, iniciar sesion o salir
    Parametros: Ninguno
    Retorna: Nada
    """
    usuario_logueado = None
    opcion = "0"
    while opcion != "6":
        print("===VUELOS====")
        print("1. Registrarse")
        print("2. Iniciar sesión")
        print("3. Salir")
        print("4. Agregar Vuelo")
        print("5. Eliminar Vuelo")
        print("6. Reservar Vuelo")
        print("7. Ver Reservas")
        print("8. Buscar Vuelos")  
        print("9. Mostrar vuelos")
        opcion = input("Elegí una opción: ")

        if opcion == "1":
            RegistrarUsuario()
        elif opcion == "2":
            usuario_logueado = Login()
            if usuario_logueado is not None:
                print(f" Usuario logueado: {usuario_logueado}")
        elif opcion == "3":
            print(" ¡Hasta luego!\n")
            break
        elif opcion == "4":
            agregarVuelo()
        elif opcion == "5":
            eliminar_vuelo()
        elif opcion == "6":
            reservar_vuelo(usuario_logueado)
            break
        elif opcion == "7":
            ver_reservas(usuario_logueado)
        elif opcion == "8":
            busquedaVuelos()
        elif opcion == "9":
            print(vuelos)

        else:
            print("Opcion invalida. \n")

if __name__ == "__main__":
    main()
