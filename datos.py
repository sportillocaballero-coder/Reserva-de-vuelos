import os
import json

def crearDirectorio(ruta_directorio):
    """Crea un directorio si no existe"""
    if not os.path.exists(ruta_directorio):
        os.makedirs(ruta_directorio)

def cargarArchivo(datos, nombre_archivo):
    """Guarda datos en un archivo JSON"""
    try:
        # Asegurar que exista el directorio datos
        directorio = os.path.join(os.path.dirname(__file__), "datos")
        crearDirectorio(directorio)
        
        ruta_archivo = os.path.join(directorio, nombre_archivo)
        with open(ruta_archivo, 'w', encoding='utf-8') as archivo:
            json.dump(datos, archivo, indent=4, ensure_ascii=False)
        return True
    except Exception as e:
        print(f"Error al guardar: {e}")
        return False

def leerArchivo(nombre_archivo):
    """Lee y retorna los datos"""
    try:
        ruta_archivo = os.path.join(os.path.dirname(__file__), "datos", nombre_archivo)
        with open(ruta_archivo, 'r', encoding='utf-8') as archivo:
            return json.load(archivo)
    except FileNotFoundError:
        return {"usuarios": [], "contrasenas": []}
    except Exception as e:
        print(f"Error al leer: {e}")
        return {"usuarios": [], "contrasenas": []}
