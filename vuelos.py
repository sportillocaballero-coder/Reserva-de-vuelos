import random
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

# Validar fecha
def validar_fecha(fecha):
    #Si o si tiene que tener 10 caracteres
    if len(fecha) != 10:
        return False

    #Verifica que tenga / 
    if fecha[2] != "/" or fecha[5] != "/":
        return False

    #Separa por posiciones (0 y 2 toman las posiciones 0 y 1, el 2 no cuenta)
    dia = fecha[0:2]
    mes = fecha[3:5]
    anio = fecha[6:10]

    #Comprueba los numeros
    if not (dia.isdigit() and mes.isdigit() and anio.isdigit()):
        return False

    #Lo convierte a entero
    dia = int(dia)
    mes = int(mes)
    anio = int(anio)

    #lA validacion
    if anio < 2024:
        return False
    if mes < 1 or mes > 12:
        return False
    if dia < 1 or dia > 31:
        return False

    #Meses con 30 dias
    if mes in (4, 6, 9, 11) and dia > 30:
        return False

    #Febrero, sin bisiesto
    if mes == 2 and dia > 29:
        return False

    return True

# asientos 
def generar_matriz_asientos(total_asientos):
    """
    Genera una matriz de asientos típica de avión:
    - 6 asientos por fila (3-3)
    - Filas calculadas según total de asientos

    IMPORTANTE: Esta es la matriz que genera, la que muestra la pantalla esta en reservas.py
    """
    columnas = 6  #3 asientos - pasillo - 3 asientos
    filas = (total_asientos + columnas - 1) // columnas  # redondeo hacia arriba
    return [[0 for _ in range(columnas)] for _ in range(filas)]

"""
Persistencia de vuelos con json:
- Los vuelos se guardan en datos/vuelos.json como lista
- Al iniciar, se cargan desde el archivo
"""
VUELOS_DIR = os.path.join(os.path.dirname(__file__), "datos")
VUELOS_FILE = os.path.join(VUELOS_DIR, "vuelos.json")

def leerVuelosJson():
    try:
        if not os.path.exists(VUELOS_FILE):
            return []
        with open(VUELOS_FILE, 'r', encoding='utf-8') as f:
            data = json.load(f)
            if isinstance(data, dict):
                return [data]
            if isinstance(data, list):
                return data
            return []
    except Exception as e:
        print(f"Error al leer vuelos: {e}")
        return []

def guardarVuelos(lista):
    try:
        if not os.path.exists(VUELOS_DIR):
            os.makedirs(VUELOS_DIR)
        with open(VUELOS_FILE, 'w', encoding='utf-8') as f:
            json.dump(lista, f, indent=4, ensure_ascii=False)
        return True
    except Exception as e:
        print(f"Error al guardar vuelos: {e}")
        return False

#Ayuda a persistir los vuelos, toma la lista de vuelos
def save_vuelos():
    return guardarVuelos(vuelos)

# Lista global cargada desde el archivo
vuelos = leerVuelosJson()

def agregarVuelo():
    #TODO: persistir vuelos en archivo JSON1
    #TODO: validar que precio y asientos sean números válidos
    #TODO: agregar matriz de asientos para cada vuelo
    """
    Objetivo: Agregar un nuevo vuelo al sistema si no existe uno igual.
    Parametros: Ninguno.
    Retorna: Nada.
    """
    origen = input("Origen: ").strip()
    destino = input("Destino: ").strip()
    fecha = input("Fecha (DD/MM/AAAA): ").strip()
    if not validar_fecha(fecha):
        print("Formato de fecha incorrecto")
        return

    precio = input("Precio: ").strip()
    if precio.replace(".", "", 1).isdigit():   # permite un solo punto decimal
        precio = float(precio)
        if precio <= 0:
            print("El precio debe ser mayor a 0")
            return
    else:
        print("Precio inválido")
        return

    asientos = input("Asientos: ").strip()
    if asientos.isdigit():
        asientos = int(asientos)
        if asientos <= 0:
            print("Debe haber al menos 1 asiento")
            return
    else:
        print("Cantidad de asientos inválida")
        return

    vuelo = {
        "id": f"{random.randint(1000, 9999)}",
        "origen": origen,
        "destino": destino,
        "fecha": fecha,
        "precio": precio,
        "asientos": asientos,
        "matriz": generar_matriz_asientos(asientos)  # genera matriz basada en total de asientos
    }

    # evitar duplicados (origen+destino+fecha)
    for v in vuelos:
        if v.get("origen") == origen and v.get("destino") == destino and v.get("fecha") == fecha:
            print("Ese vuelo ya existe")
            return

    vuelos.append(vuelo)
    if save_vuelos():
        print("Vuelo agregado con exito")
    else:
        print("Vuelo agregado, pero no se pudo guardar en disco")

def eliminarVuelo():
    #TODO: Guardar cambios en archivos JSON
    """
    Objetivo: Eliminar un vuelo del sistema por su ID.
    Parametros: Ninguno.
    Retorna: Nada.
    """
    if not vuelos:
        print("No hay vuelos cargados")
        return

    vid = input("ID del vuelo a eliminar: ").strip()
    idx = None
    for i in range(len(vuelos)):
        if str(vuelos[i]["id"]) == str(vid):
            idx = i
            break

    if idx is not None:
        del vuelos[idx]
        if save_vuelos():
            print("Vuelo eliminado con exito")
        else:
            print("Vuelo eliminado, pero no se pudo guardar")
    else:
        print("Vuelo no encontrado")

def busquedaVuelos():
    """
    Objetivo: Mostrar los vuelos disponibles y permitir seleccionar uno.
    Parametros: Ninguno.
    Retorna: Nada.
    """
    if not vuelos:
        print("No hay vuelos cargados")
        return

    print("\n--- Vuelos disponibles ---")
    for idx, vuelo in enumerate(vuelos, 1):
        print(f"{idx}. ID: {vuelo['id']} | Origen: {vuelo.get('origen','-')} | Destino: {vuelo['destino']} | Fecha: {vuelo['fecha']} | Precio: {vuelo['precio']} | Asientos: {vuelo['asientos']}")

    seleccion = input(f"Seleccione el vuelo por su numero (1 a {len(vuelos)}), o Enter para salir: ").strip()
    if seleccion.isdigit():
        seleccion = int(seleccion)
        if 1 <= seleccion <= len(vuelos):
            vuelo = vuelos[seleccion - 1]
            print(f"Seleccionaste vuelo ID {vuelo['id']}, origen {vuelo.get('origen','-')} y destino {vuelo['destino']}")
        else:
            print("Seleccion invalida")
    elif seleccion == "":
        print("Saliendo de la busqueda de vuelos")
    else:
        print("Seleccion invalida")

