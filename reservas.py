from vuelos import vuelos   #Para acceder a la lista de vuelos


reservas = [{"id":123,"usuario":"pepe","vuelo":4321,"cant":2}]
vecesReservado = [{"id":123,"contador":4},{"id":321,"contador":2},{"id":444,"contador":8}]

def mostrar_matriz_asientos(matriz):
    """
    Muestra la matriz de asientos con formato típico (A1, A2, ..., B1, B2, ...)
    0 = libre, 1 = ocupado
    """
    filas = len(matriz)
    columnas = len(matriz[0]) if filas > 0 else 0
    letras = [chr(ord('A') + i) for i in range(filas)]
    print("Asientos: (0=libre, 1=ocupado)")

    
    for i, fila in enumerate(matriz):
        fila_str = letras[i] + " "
        for j, asiento in enumerate(fila):
            fila_str += f"{asiento} "
        print(fila_str + "  " + " ".join([f"{letras[i]}{j+1}" for j in range(columnas)]))

def reservarVuelo(usuario):

#TODO:validar que no reserve mas asientos de los disponibles ####EN PROCESO #####
#TODO: permitir elegir asiento especifico dentro de una  matriz
#TODO: guardar reserva en archivo JSON
#TODO Mostrar el precio al reservar asiento
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
    vuelo = None
    for v in vuelos:
        if v["id"] == vid:
            vuelo = v
    if not vuelo:
        print("Vuelo no encontrado")
        return

    matriz = vuelo.get("matriz")
    if not matriz:
        print("Este vuelo no tiene matriz de asientos definida.")
        return

    mostrar_matriz_asientos(matriz)
    cant = input("Cantidad de asientos: ")
    if not cant.isdigit():
        print("Cantidad invalida")
        return
    cant = int(cant)
    libres = sum(asiento == 0 for fila in matriz for asiento in fila)
    if libres < cant:
        print(f"Solo hay {libres} asientos libres")
        return

    seleccionados = []
    letras = [chr(ord('A') + i) for i in range(len(matriz))]
    columnas = len(matriz[0])
    for n in range(cant):
        while True:
            asiento_str = input(f"Elija asiento #{n+1} (ejemplo A1, B3): ").upper().strip()
            if len(asiento_str) < 2:
                print("Formato incorrecto")
                continue
            fila_letra = asiento_str[0]
            col_num = asiento_str[1:]
            if fila_letra not in letras or not col_num.isdigit():
                print("Formato incorrecto")
                continue
            fila_idx = letras.index(fila_letra)
            col_idx = int(col_num) - 1
            if not (0 <= fila_idx < len(matriz) and 0 <= col_idx < columnas):
                print("Asiento fuera de rango")
                continue
            if matriz[fila_idx][col_idx] == 1:
                print("Ese asiento ya está ocupado")
                continue
            if (fila_idx, col_idx) in seleccionados:
                print("Ya seleccionaste ese asiento")
                continue
            seleccionados.append((fila_idx, col_idx))
            break

    # Marcar asientos como ocupados
    for fila_idx, col_idx in seleccionados:
        matriz[fila_idx][col_idx] = 1
    vuelo["asientos"] -= cant

    reserva = {
        "id": f"R{len(reservas)+1:04d}",
        "usuario": usuario,
        "vuelo": vid,
        "cant": cant,
        "asientos": [f"{letras[fila]}{col+1}" for fila, col in seleccionados]
    }

    reservas.append(reserva)
    idABuscar = reserva["id"]
    estaReservado = any(objeto["id"] == idABuscar for objeto in vecesReservado)

    if estaReservado:
        for reservaAComparar in vecesReservado:
            if reservaAComparar["id"] == idABuscar:
                reservaAComparar["contador"] = reserva["contador"] + 1
    else:
        vecesReservado.append({"id":idABuscar,"vecesReservado": 1})

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

#########Funcion de pagar reserva NUEVO#########
pagar_reserva = lambda reservas, id_reserva: [
    {**r, "estado": "pagada"} if r["id"] == id_reserva and r["estado"] == "pendiente" else r
    for r in reservas
]


#TODO: permitir cancelar reserva y devolver asientos al vuelo
#TODO: permitir pagar reserva (cambiar el estado a "pagada")##### (EN PROCESO)#######
#TODO: historial de reservas mas ordenada
#TODO: estadisticas con lambda > calcular total el total de los asientos, reservados

#TODO: usar listas por comprension para:
#- obtener todas las reservas de un usuario
#- calcular el total de asientos reservados con sum()
#- obtener todos los IDs de vuelos reservados