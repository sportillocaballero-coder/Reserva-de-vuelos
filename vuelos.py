import random
from datetime import datetime
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
def validar_fecha(fecha: str) -> bool:
    if len(fecha) != 10:
        return False
    if fecha[2] != "/" or fecha[5] != "/":
        return False
    dia, mes, anio = fecha[:2], fecha[3:5], fecha[6:]
    if not (dia.isdigit() and mes.isdigit() and anio.isdigit()):
        return False
    dia, mes, anio = int(dia), int(mes), int(anio)
    # sin contemplar febrero bisiesto
    if not (1 <= dia <= 31 and 1 <= mes <= 12 and anio >= 2024):
        return False
    return True

# asientos 
def generar_matriz_asientos(total_asientos):
    """
    Genera una matriz de asientos típica de avión:
    - 6 asientos por fila (3-3)
    - Filas calculadas según total de asientos
    """
    columnas = 6  # configuración típica: 3 asientos - pasillo - 3 asientos
    filas = (total_asientos + columnas - 1) // columnas  # redondeo hacia arriba
    return [[0 for _ in range(columnas)] for _ in range(filas)]

# Lista global de vuelos (IDs como strings y con 'origen' para evitar KeyError)
vuelos = [
    {
        "id": "1001",
        "origen": "CBA",
        "destino": "BS",
        "fecha": "10/09/2024",
        "precio": 1234.0,
        "asientos": 40,
        "matriz": generar_matriz_asientos(40)
    },
    {
        "id": "1002",
        "origen": "BUE",
        "destino": "BL",
        "fecha": "15/10/2024",
        "precio": 1275.0,
        "asientos": 50,
        "matriz": generar_matriz_asientos(50)
    },
    {
        "id": "1003",
        "origen": "ROS",
        "destino": "PR",
        "fecha": "20/11/2024",
        "precio": 874.0,
        "asientos": 70,
        "matriz": generar_matriz_asientos(70)
    }
]

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

    # evitar duplicados
    for v in vuelos:
        if v["origen"] == origen and v["destino"] == destino and v["fecha"] == fecha:
            print("Ese vuelo ya existe")
            return

    #vuelos.append(vuelo)
    cargarArchivo(vuelo,"vuelos.json")
    print("Vuelo agregado con exito")

def eliminarVuelo():
    #TODO: Permitir filtrar vuelos por fehca
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
        print("Vuelo eliminado con exito")
    else:
        print("Vuelo no encontrado")

def busquedaVuelos():
    #TODO: Filtrar vuelos por destino
    #TODO: Filtrar vuelos por fecha
    #TODO: Usar lambda para ordenar vuelos por precio
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

# Funciones utilitarias (no interactúan al importar)
def listar_vuelos(orden: str = "ninguno"):
    """
    Retorna la lista de vuelos, opcionalmente ordenada por precio:
    orden = "asc", "desc", o "ninguno"
    """
    lista = vuelos.copy()
    if orden == "asc":
        lista.sort(key=lambda v: v["precio"])
    elif orden == "desc":
        lista.sort(key=lambda v: v["precio"], reverse=True)
    return lista

# Removed: funciones vuelo_mas_caro, vuelo_mas_barato y vuelo_mas_reservado
# Estas funciones están duplicadas en estadistica.py. Usar las funciones definidas en ese módulo
# (importando estadistica.vueloCaro / vueloBarato / vueloMasReservado) cuando se necesiten.

# IDs de vuelos
ids = [v["id"] for v in vuelos]

# Vuelos con precio mayor a 500
caros = [v for v in vuelos if v["precio"] > 500]

# Lista de (origen, destino)
rutas = [(v["origen"], v["destino"]) for v in vuelos]
