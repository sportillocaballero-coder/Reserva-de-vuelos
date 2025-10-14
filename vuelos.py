import random
from datetime import datetime

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
def generar_matriz_asientos(filas, columnas):
    return [[0 for _ in range(columnas)] for _ in range(filas)] #El 0 puede significar asiento libre y 1 ocupado.
# Lista global de vuelos
vuelos = []

def agregarVuelo():
#TODO: persistir vuelos en archivo JSON
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
        "matriz": generar_matriz_asientos(asientos // 6, 6)  # ejemplo
    }

    # evitar duplicados
    for v in vuelos:
        if v["origen"] == origen and v["destino"] == destino and v["fecha"] == fecha:
            print("Ese vuelo ya existe")
            return

    vuelos.append(vuelo)
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
        if vuelos[i]["id"] == vid:
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
        print(f"{idx}. ID: {vuelo['id']} | Origen: {vuelo['origen']} | Destino: {vuelo['destino']} | Fecha: {vuelo['fecha']} | Precio: {vuelo['precio']} | Asientos: {vuelo['asientos']}")

    seleccion = input(f"Seleccione el vuelo por su numero (1 a {len(vuelos)}), o Enter para salir: ").strip()
    if seleccion.isdigit():
        seleccion = int(seleccion)
        if 1 <= seleccion <= len(vuelos):
            vuelo = vuelos[seleccion - 1]
            print(f"Seleccionaste vuelo ID {vuelo['id']}, origen {vuelo['origen']} y destino {vuelo['destino']}")
        else:
            print("Seleccion invalida")
    elif seleccion == "":
        print("Saliendo de la busqueda de vuelos")
    else:
        print("Seleccion invalida")

#criterio = input("Filtrar por (d=destino, f=fecha, n=ninguno): ").strip().lower()
#filtro = None
#if criterio == "d":
 #   filtro = input("Destino: ").strip()
  #  lista = [v for v in vuelos if v["destino"].lower() == filtro.lower()]
#elif criterio == "f":
 #   filtro = input("Fecha (DD/MM/AAAA): ").strip()
  #  lista = [v for v in vuelos if v["fecha"] == filtro]
#else:
 #   lista = vuelos


#ordenar por precio
orden = input("¿Ordenar por precio? (asc/desc/ninguno): ").strip().lower()
if orden == "asc":
    lista.sort(key=lambda v: v["precio"])
elif orden == "desc":
    lista.sort(key=lambda v: v["precio"], reverse=True)

#vuelo más caro
mas_caro = max(vuelos, key=lambda v: v["precio"])

#vuelo más barato
mas_barato = min(vuelos, key=lambda v: v["precio"])

#vuelo más reservado
mas_reservado = min(vuelos, key=lambda v: v["asientos"])


#TODO: usar listas por comprension para:
#- obtener solo los IDs de los vuelos
#- filtrar vuelos por precio mayor a un valor dado
#- generar lista de (origen, destino) de todos los vuelos

# IDs de vuelos
ids = [v["id"] for v in vuelos]

# Vuelos con precio mayor a 500
caros = [v for v in vuelos if v["precio"] > 500]

# Lista de (origen, destino)
rutas = [(v["origen"], v["destino"]) for v in vuelos]
