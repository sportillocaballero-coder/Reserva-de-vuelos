import random

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
    precio = float(input("Precio: ").strip())
    asientos = int(input("Asientos: ").strip())

    vuelo = {
        "id": f"{random.randint(1000, 9999)}",
        "origen": origen,
        "destino": destino,
        "fecha": fecha,
        "precio": precio,
        "asientos": asientos
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

#TODO: usar listas por comprension para:
#- obtener solo los IDs de los vuelos
#- filtrar vuelos por precio mayor a un valor dado
#- generar lista de (origen, destino) de todos los vuelos