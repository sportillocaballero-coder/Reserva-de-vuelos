import re
from datos import leerArchivo, cargarArchivo
from reservas import archivoReserva, leerReservasJson

#cargar datos al iniciar
datos_usuarios = leerArchivo("usuarios.json")
usuarios = datos_usuarios["usuarios"]
contrasenas = datos_usuarios["contrasenas"]

"""
- Si el archivo está vacío
if not isinstance(datos_usuarios, dict):
datos_usuarios = {"usuarios": [], "contrasenas": []}

- Siempre en listas
if not isinstance(usuarios, list): usuarios = []
if not isinstance(contrasenas, list): contrasenas = []
"""

def guardarCambios():
    """Guarda los cambios en el archivo JSON"""
    datos = {
        "usuarios": usuarios,
        "contrasenas": contrasenas
    }
    return cargarArchivo(datos, "usuarios.json")

def verificar_caracter_especial(password):
    """
    Objetivo: Verificar si una contrasena contiene al menos un caracter especial.
    Parametros:
    - password (str): Contrasena a verificar.
    Retorna: bool - True si contiene caracter especial, False en caso contrario.
    """
    patron_especial = r'[^a-zA-Z0-9\s]'
    return re.search(patron_especial, password) is not None

def registrarUsuario():
    """
    Objetivo: Registrar un nuevo usuario en el sistema.
    Parametros: Ninguno.
    Retorna: Nada.
    """
    print("\n--Registro--")
    
    nuevo_usuario = input("Ingrese un nombre de usuario: ").strip()
    while not nuevo_usuario:
        print("ERROR: el nombre de usuario no puede estar vacio")
        nuevo_usuario = input("Ingrese un nombre de usuario: ").strip()

    if nuevo_usuario in usuarios:
        print("Ese usuario ya esta registrado\n")
    else:
        nueva_contrasena = input("Ingrese una contrasena, debe tener un caracter especial: ").strip()
        while not nueva_contrasena or not verificar_caracter_especial(nueva_contrasena):
            if not nueva_contrasena:
                print("ERROR: la contrasena no puede estar vacia")
            else:
                print("ERROR: la contrasena debe tener un caracter especial (!, #, ?, etc...)")
            nueva_contrasena = input("Ingrese una contrasena: ").strip()
        usuarios.append(nuevo_usuario)
        contrasenas.append(nueva_contrasena)
        if guardarCambios():
            print("Registro exitoso y guardado\n")
        else:
            print("Registro exitoso pero no se pudo guardar en disco\n")

def login():
    """
    Objetivo: Autenticar a un usuario registrado en el sistema.
    Parametros: Ninguno.
    Retorna: str - Nombre del usuario si el login es exitoso, None en caso contrario.
    """
    print("\n--- Iniciar Sesion ---")
    
    usuario = input("Usuario: ").strip()
    while not usuario:
        print("ERROR: el usuario no puede estar vacio")
        usuario = input("Usuario: ").strip()
    
    contrasena = input("Contrasena: ").strip()
    while not contrasena:
        print("ERROR: la contrasena no puede estar vacia")
        contrasena = input("Contrasena: ").strip()

    if usuario not in usuarios:
        print("El usuario no existe\n")
        return None
    
    i = usuarios.index(usuario)
    if contrasenas[i] == contrasena:
        print(f"Bienvenido: {usuario}\n")
        return usuario
    else:
        print("Contrasena incorrecta\n")
        return None


def cambiarContrasena(usuario):
    """
    Objetivo: Cambiar la contrasena de un usuario existente
    Parametros:
    - usuario (str): Nombre del usuario 
    Retorna: Nueva contraseña
    """
    if usuario not in usuarios:
        print("Usuario no encontrado")
        return

    i = usuarios.index(usuario)

    actual = input("Ingrese su contrasena actual: ").strip()
    if actual != contrasenas[i]:
        print("Contrasena actual incorrecta")
        return

    nueva = input("Ingrese la nueva contrasena (debe tener un caracter especial): ").strip()
    while not verificar_caracter_especial(nueva):
        print("ERROR: la contrasena debe tener un caracter especial (!, #, ?, etc...)")
        nueva = input("Ingrese una contrasena válida: ").strip()

    contrasenas[i] = nueva
    if guardarCambios():
        print("Contrasena actualizada correctamente")
    else:
        print("Contrasena actualizada, pero no se pudo guardar en disco")

def cambiarNombreUsuario(usuario):
    """
    Objetivo: Cambia nombre de usuario
    Parametros:
    - usuario (str): Nombre del usuario
    Retorna: str - Nuevo nombre de usuario si es valido y si no None en caso de que no.
    """
    if usuario not in usuarios:
        print("Usuario no encontrado")
        return None

    i = usuarios.index(usuario)

    nuevo_nombre = input("Ingrese el nuevo nombre de usuario: ").strip()

    if not nuevo_nombre:
        print("El nombre de usuario no puede estar vacío")
        return None

    if nuevo_nombre in usuarios:
        print("Ese nombre ya existe")
        return None

    usuarios[i] = nuevo_nombre

    todas_las_reservas = leerReservasJson()

    for reserva in todas_las_reservas:
        # Si la reserva pertenece al nombre ANTIGUO, lo actualizamos
        if reserva.get("usuario") == usuario:
            reserva["usuario"] = nuevo_nombre
    
    archivoReserva(todas_las_reservas)

    if guardarCambios():
        print(f"Nombre de usuario actualizado correctamente a: {nuevo_nombre}")
        return nuevo_nombre
    else:
        print("Nombre actualizado, pero no se guardo")
        return nuevo_nombre

# def editarPerfil(usuario):
#     """
#     Objetivo: Editar el perfil completo del usuario completo, nombre y contraseña
#     Parametros:
#     - usuario (str): Nombre de usuario
#     Retorna: str - Nuevo nombre de usuario si es q cambio, usuario original si no cambio, None si es que falla.
#     """
#     if usuario not in usuarios:
#         print("Usuario no encontrado")
#         return None

#     i = usuarios.index(usuario)
#     usuario_actualizado = usuario

#     print("\n--- Editar Perfil ---")
#     cambiar_nombre = input("¿Desea cambiar su nombre de usuario? (s/n): ").strip().lower()
    
#     if cambiar_nombre == "s":
#         nuevo_nombre = input("Ingrese el nuevo nombre de usuario: ").strip()
        
#         if not nuevo_nombre:
#             print("El nombre de usuario no puede estar vacío")
#         elif nuevo_nombre in usuarios:
#             print("Ese nombre ya existe")
#         else:
#             usuarios[i] = nuevo_nombre
#             usuario_actualizado = nuevo_nombre
#             print(f"Nombre actualizado a: {nuevo_nombre}")

#     cambiar_pass = input("¿Desea cambiar su contraseña? (s/n): ").strip().lower()
    
#     if cambiar_pass == "s":
#         nueva = input("Ingrese la nueva contraseña (debe tener un caracter especial): ").strip()
#         while not verificar_caracter_especial(nueva):
#             print("ERROR: la contraseña debe tener un caracter especial (!, #, ?, etc...)")
#             nueva = input("Ingresar una contraseña valida: ").strip()
        
#         i_actual = usuarios.index(usuario_actualizado)
#         contrasenas[i_actual] = nueva
#         print("Contraseña actualizada")

#     if guardarCambios():
#         print("Perfil actualizado correctamente")
#     else:
#         print("Perfil actualizado pero no se guardo")
    
#     return usuario_actualizado