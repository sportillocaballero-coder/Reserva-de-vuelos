import re
from datos import leerArchivo, cargarArchivo

#cargar datos al iniciar
datos_usuarios = leerArchivo("usuarios.json")
usuarios = datos_usuarios["usuarios"]
contrasenas = datos_usuarios["contrasenas"]

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
#TODO: #TODO guardar usuarios en archivos json para la persistencia de los datos 
    """
    Objetivo: Registrar un nuevo usuario en el sistema.
    Parametros: Ninguno.
    Retorna: Nada.
    """
    print("\n--Registro--")
    nuevo_usuario = input("Ingrese un nombre de usuario: ").strip()


    if nuevo_usuario in usuarios:
        print("Ese usuario ya esta registrado\n")
    else:
        nueva_contrasena = input("Ingrese una contrasena, debe tener un caracter especial: ").strip()
        while not verificar_caracter_especial(nueva_contrasena):
            print("ERROR: la contrasena debe tener un caracter especial (!, #, ?, etc...)")
            nueva_contrasena = input("Ingrese una contrasena: ").strip()
        usuarios.append(nuevo_usuario)
        contrasenas.append(nueva_contrasena)
        if guardarCambios():
            print("Registro exitoso y guardado\n")
        else:
            print("Registro exitoso pero no se pudo guardar en disco\n")

def login():
#TODO: cargar la lista de archivos JSON antes de validar
    """
    Objetivo: Autenticar a un usuario registrado en el sistema.
    Parametros: Ninguno.
    Retorna: str - Nombre del usuario si el login es exitoso, None en caso contrario.
    """
    print("\n--- Iniciar Sesion ---")
    try:
        usuario = input("Usuario: ").strip()
        contrasena = input("Contrasena: ").strip()

        if not usuario or not contrasena:
            print("Usuario y contraseña no pueden estar vacíos\n")
            return None

        i = usuarios.index(usuario) 
        if contrasenas[i] == contrasena:  
            print(f"Bienvenido/a, {usuario}\n")
            return usuario
        else:
            print("Contraseña incorrecta\n")
            
    except ValueError:
        print("El usuario no existe\n")
    except IndexError:
        print("Error en el sistema\n")
    except Exception as e:
        print("Error inesperado")
    
    return None
#TODO: usar listas por comprension para:
#- obtener lista de usuarios en mayusculas
#- filtrar usuarios por alguna condicion (ej: que empiecen con una letra)


#TODO: permitir que como usuario cambiemos de contraseñas
#TODO: #TODO permitir que el usuario edite sus datos de perfil

