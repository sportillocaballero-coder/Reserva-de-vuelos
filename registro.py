import random, re
# La lista paralelas, aca se guardan el usuario y contraseña de los clientes por posicion 
usuarios = []
contraseñas = []
vuelos = []
reservas = []

def verificar_caracter_especial(password):
    """Verifica si la contraseña contiene al menos un carácter especial."""
    # Patrón que busca CUALQUIER COSA que no sea letra, número o espacio.
    patron_especial = r'[^a-zA-Z0-9\s]' 
    
    # re.search() devuelve un objeto match si encuentra el patrón, sino devuelve None.
    if re.search(patron_especial, password):
        return True  # Carácter especial encontrado
    else:
        return False # No hay caracteres especiales

#Se registran los clientes
def registrarUsuario():
    """
    Objetivo: Registrar un nuevo usuario y contraseña si el usuario no existe.
    Parámetros: Ninguno (usa input).
    Retorna: Nada.
    """ 
    print("\n--Registro--")
    nuevo_usuario = input("Ingrese un nombre de usuario: ").strip()

    if nuevo_usuario in usuarios:
        print("Ese usuario ya esta registrado\n")
    else:
        nueva_contraseña = input("Ingrese una contraseña, la contraseña debe tener un caracter especial: ").strip()
        verificarCaracter = verificar_caracter_especial(nueva_contraseña)
        while verificarCaracter == False:
            print("ERROR, la contraseña debe de tener un caracter especial (!, #, ?, etc...)")
            nueva_contraseña = input("Ingrese una contraseña, la contraseña debe tener un caracter especial: ").strip()
            verificarCaracter = verificar_caracter_especial(nueva_contraseña)
        usuarios.append(nuevo_usuario)
        contraseñas.append(nueva_contraseña)
        print("Registro exitoso\n")

# Login de clientes
def login():
    """
    Objetivo: Permitir que un usuario registrado inicie sesión.
    Parámetros: Ninguno (usa input).
    Retorna:
      - str: Nombre de usuario si el login es exitoso.
      - None: Si falla el login.
    """
    print("\n--- Iniciar Sesion ---")
    usuario = input("Usuario: ").strip()
    contraseña = input("Contraseña: ").strip()

    if usuario in usuarios:
        i = usuarios.index(usuario)
        if contraseñas[i] == contraseña:
            print(f"Bienvenido/a, {usuario}\n")
            return usuario
        else:
            print("Contraseña incorrecta\n")
    else:
        print("El usuario no existe\n")

    return None

def agregarVuelo():
    """
    Objetivo: Agregar un nuevo vuelo si el usuario está logueado y no existe un vuelo igual (origen, destino, fecha).
    Parámetros: Ninguno (usa input y variable global usuario).
    Retorna: Nada.
    """
    if not usuarios:
        print(" Tenes que iniciar sesion")
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
            print("Ese vuelo ya existe")
            return

    vuelos.append(vuelo)
    print("Vuelo agregado con exito")

def reservarVuelo(usuario):
    """
    Objetivo: Permitir a un usuario reservar asientos en un vuelo existente.
    Parámetros:
      - usuario (str): Usuario logueado.
    Retorna: Nada.
    """
    if not usuario:
        print(" Tenes que iniciar sesion")
        return

    if not vuelos:
        print("No hay vuelos cargados")
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
        print("Vuelo no encontrado")
        return
    if vuelo["asientos"] < cant:
        print(f"Solo hay {vuelo['asientos']} asientos")
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

    print(" Reserva creada:", reserva)

def verReserva (usuario):
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
        print("No tenes reservas")

def eliminarVuelo ():
    """
    Objetivo: Eliminar un vuelo existente por su ID.
    Parámetros: Ninguno (usa input).
    Retorna: Nada.
    """
    if not vuelos:
        print("No hay vuelos cargados")
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
        print("Vuelo eliminado con exito")
    else:
        print("Vuelo no encontrado")

def busquedaVuelos():
    """
    Objetivo: Mostrar los vuelos disponibles y permitir seleccionar uno.
    Parámetros: Ninguno.
    Retorna: Nada.
    """
    if not vuelos:
        print("No hay vuelos cargados")
        return
    print("\n--- Vuelos disponibles ---")
    for idx, vuelo in enumerate(vuelos, 1):
        print(f"{idx}. ID: {vuelo['id']} | Origen: {vuelo['origen']} | Destino: {vuelo['destino']} | Fecha: {vuelo['fecha']} | Precio: {vuelo['precio']} | Asientos: {vuelo['asientos']}")
    seleccion = input(f"Seleccione el vuelo por su numero (1 a {len(vuelos)}), o presione Enter para salir: ")
    if seleccion.isdigit():
        seleccion = int(seleccion)
        if 1 <= seleccion <= len(vuelos):
            vuelo = vuelos[seleccion - 1]
            print(f"Usted ha seleccionado el vuelo con ID {vuelo['id']}, origen {vuelo['origen']} y destino {vuelo['destino']}\n")
        else:
            print("Seleccion invalida")
    elif seleccion.strip() == "":
        print("Saliendo de la busqueda de vuelos")
    else:
        print("Seleccion invalida")

def menuVuelos(usuario):
    opcion = "0"
    while opcion != "5":
        print(f"\n=== BIENVENIDO ({usuario}) ===")
        print("1. Reserva tu vuelo")
        print("2. Ver mis reservas")
        print("3. Buscar vuelos")
        print("4. Mostrar vuelos")
        print("5. Salir")

        opcion = input("Seleccione una opcion: ").strip()

        if opcion == "1":
            reservarVuelo(usuario)
        if opcion == "2":
            verReserva(usuario)
        elif opcion == "3":
            busquedaVuelos(usuario)
        elif opcion == "4":
            print(vuelos) #TODO: Ordenar mejor esta opcion, no esta bien graficamente 
        elif opcion == "5":
            print(f"Hasta pronto {usuario}")
        else:
            print("Opcion invalida")

#TODO: Al entrar al modoAdmin, la interfaz se junta junto al de menuPrincipal. Esto no debe de ser asi 
def modoAdmin ():
    print("\n-- Administracion --")

    #Se utilizara ahora una validacion basica para 
    user = input("Usuario del Admin: ").strip()
    password = input("Contraseña: ").strip()

    #Palabra clave para inicio de sesion 
    #TODO: Mejorar esta funcion, por ejemplo que sea oculto, pero varios puedan tener acceso, y tambien permitir dar permisos a usuarios del sistema
    if user == "admin" and password == "1234":
        print("Acceso admitido")

        print(f"\nBienvenido admin") #TODO: Modificar mas adelante 
        print("1. Agregar un Vuelo al Sistema")
        print("2. Mostrar Vuelos ")
    else: 
        print("Credenciales invalidas")


def menuPrincipal ():
    opcion = "0"
    while opcion != "4":
        print("=== MENU PRINCIPAL ===")
        print("1. Registrate")
        print("2. Login")
        print("3. Modo Admin")
        print("4. Salir")

        opcion = input("Seleccione una opcion: ").strip()
        if opcion == "1":
            registrarUsuario()
        if opcion == "2":
            usuario = login()
            if usuario is not None:
                menuVuelos(usuario) #Este el menu de vuelos 
        if opcion == "3":
            modoAdmin()
        elif opcion == "4":
            print("Nos vemos!")
if __name__ == "__main__":
    menuPrincipal()
