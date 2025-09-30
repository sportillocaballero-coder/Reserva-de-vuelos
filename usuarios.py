import re

usuarios = []
contrasenas = []

def verificar_caracter_especial(password):
    patron_especial = r'[^a-zA-Z0-9\s]'
    return re.search(patron_especial, password) is not None

def registrarUsuario():
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
        print("Registro exitoso\n")

def login():
    print("\n--- Iniciar Sesion ---")
    usuario = input("Usuario: ").strip()
    contrasena = input("Contrasena: ").strip()

    if usuario in usuarios:
        i = usuarios.index(usuario)
        if contrasenas[i] == contrasena:
            print(f"Bienvenido/a, {usuario}\n")
            return usuario
        else:
            print("Contrasena incorrecta\n")
    else:
        print("El usuario no existe\n")
    return None