from vuelos import vuelos   #Para acceder a la lista de vuelos


reservas = []

def reservarVuelo(usuario):

#TODO: validar que no reserve mas asientos de los disponibles
#TODO: permitir elegir asiento especifico dentro de una  matriz
#TODO: guardar reserva en archivo JSON
    """
    Objetivo: Permitir a un usuario reservar asientos en un vuelo existente.
    Parametros:
      - usuario (str): Usuario logueado.
    Retorna: Nada.
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
#TODO: permitir filtrar reservas por estado (pendiente, pagada, cancelada)
#TODO: mostrar reservas ordenadas por fecha
    """
    Objetivo: Mostrar todas las reservas realizadas por el usuario.
    Parametros:
      - usuario (str): Usuario logueado.
    Retorna: Nada.
    """

    print(f"\n-- Reservas de {usuario} --")
    tiene = False
    for r in reservas:
        if r["usuario"] == usuario:
            print(r)
            tiene = True
    if not tiene:
        print("No tenes reservas")

#TODO: permitir cancelar reserva y devolver asientos al vuelo
#TODO: permitir pagar reserva (cambiar el estado a "pagada")
#TODO: historial de reservas mas ordenada
#TODO: estadisticas con lambda > calcular total el total de los asientos, reservados

#TODO: usar listas por comprension para:
#- obtener todas las reservas de un usuario
#- calcular el total de asientos reservados con sum()
#- obtener todos los IDs de vuelos reservados