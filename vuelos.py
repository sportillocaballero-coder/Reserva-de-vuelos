import random

# Lista global de vuelos
vuelos = []

def agregarVuelo():
    """
    Agrega un nuevo vuelo si no existe uno igual (origen, destino, fecha).
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
    """
    Elimina un vuelo por su ID.
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
    """
    Muestra los vuelos disponibles y permite seleccionar uno.
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