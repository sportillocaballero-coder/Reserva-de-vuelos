from vuelos import vuelos   #Para acceder a la lista de vuelos

reservas = []

def reservarVuelo(usuario):
    """
    Permite a un usuario reservar asientos en un vuelo existente.
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

    vuelo["asientos"] -= cant

    reserva = {
        "id": f"R{len(reservas)+1:04d}",
        "usuario": usuario,
        "vuelo": vid,
        "cant": cant
    }
    reservas.append(reserva)

    print("Reserva creada:", reserva)

def verReserva(usuario):
    """
    Muestra todas las reservas realizadas por el usuario.
    """
    print(f"\n-- Reservas de {usuario} --")
    tiene = False
    for r in reservas:
        if r["usuario"] == usuario:
            print(r)
            tiene = True
    if not tiene:
        print("No tenes reservas")