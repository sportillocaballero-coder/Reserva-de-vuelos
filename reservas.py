from vuelos import vuelos, save_vuelos   #Acceso a lista de vuelos y persistencia
import random

reservas = [{"id":123,"usuario":"pepe","vuelo":4321,"cant":2}]
vecesReservado = [{"id":123,"contador":4},{"id":321,"contador":2},{"id":444,"contador":8}]

def mostrar_matriz_asientos(matriz):
    """
    Muestra la matriz de asientos con formato típico (A1, A2, ..., B1, B2, ...)
    0 = libre, 1 = ocupado

    IMPORTANTE: Esta funcion es para uso visual, muestra la matriz en la pantalla, en vuelos.py se encuentra la matriz generadora
    """
    filas = len(matriz)
    columnas = len(matriz[0])
    letras = []  #Lista de letras 

    #Se generan las letras ABCD etc
    for i in range(filas):
        letras.append(chr(ord('A') + i))

    print("Asientos: (0=libre, 1=ocupado)\n")

    for i in range(filas):
        #numeros de fila (ejemeplo: A 0 0 1 ...)
        print(letras[i], end=" ")
        for j in range(columnas):
            print(matriz[i][j], end=" ")
        print("  ", end="")

        #etiquetas de los asientos (ej: A1 A2 A3 ...)
        for j in range(columnas):
            print(letras[i] + str(j + 1), end=" ")
        print()  #salto de linea final por fila

def generarID():
    while True:
        nuevoID = random.randint(1000, 9999)
        existe = False
        for reserva in reservas:
            if reserva["id"] == nuevoID:
                existe = True
                break
        if not existe:
            return nuevoID

def reservarVuelo(usuario):
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
    vuelo = None
    for v in vuelos:
        # AJUSTE 1: comparar como texto para evitar int vs str
        if str(v["id"]) == str(vid):
            vuelo = v
    if not vuelo:
        print("Vuelo no encontrado")
        return

    matriz = vuelo.get("matriz")
    if not matriz:
        print("Este vuelo no tiene matriz de asientos definida.")
        return

    mostrar_matriz_asientos(matriz)
    
    # Calcular asientos libres en la matriz
    libres = 0
    for fila in matriz:
        for asiento in fila:
            if asiento == 0:
                libres += 1
    
    # Validar asientos disponibles en el vuelo
    asientos_disponibles = vuelo.get("asientos", 0)
    if asientos_disponibles <= 0:
        print("No hay asientos disponibles en este vuelo")
        return
    
    if libres <= 0:
        print("No hay asientos libres en este vuelo")
        return
    
    print(f"Asientos disponibles: {asientos_disponibles}")
    
    cant = input("Cantidad de asientos: ")
    if not cant.isdigit():
        print("Cantidad invalida")
        return
    cant = int(cant)
    
    if cant <= 0:
        print("Debe reservar al menos 1 asiento")
        return
    
    if cant > asientos_disponibles:
        print(f"Solo hay {asientos_disponibles} asientos disponibles para reservar")
        return
    
    if cant > libres:
        print(f"Solo hay {libres} asientos libres en la matriz")
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

    # Restar asientos disponibles
    if "asientos" in vuelo:
        vuelo["asientos"] = vuelo["asientos"] - cant
        if vuelo["asientos"] < 0:
            vuelo["asientos"] = 0

    reserva = {
        "id": generarID(),
        "usuario": usuario,
        "vuelo": vid,
        "cant": cant,
        "asientos": [f"{letras[fila]}{col+1}" for fila, col in seleccionados],
        "estado": "pendiente"  # recomendado para pagarReserva
    }

    reservas.append(reserva)
    idABuscar = reserva["id"]
    estaReservado = False
    for objeto in vecesReservado:
        if objeto["id"] == idABuscar:
            estaReservado = True
            break

    if estaReservado:
        for reservaAComparar in vecesReservado:
            if reservaAComparar["id"] == idABuscar:
                # AJUSTE 3: no existe reserva["contador"]; incrementamos el propio contador
                reservaAComparar["contador"] += 1
    else:
        # unificamos la clave con "contador" (antes había "vecesReservado")
        vecesReservado.append({"id": idABuscar, "contador": 1})

    # Persistir cambios en asientos/ocupar matriz del vuelo

    save_vuelos()


    print(f"Reserva creada( Vuelo:{reserva['vuelo']} || Asientos: {reserva['asientos']} )")

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




def get_vuelo_safe(vid):
    """Busca un vuelo por id (soporta str/int). Devuelve el dict o None."""
    try:
        from vuelos import vuelos  # usa la lista actual
    except Exception:
        return None
    for v in vuelos:
        if str(v.get("id")) == str(vid):
            return v
    return None

def cancelarReserva(usuario):
    """
    Objetivo: Cancelar una reserva del usuario y devolver los asientos al vuelo
    Parametros:
      - usuario (str): Usuario logueado
    Retorna: Cancela la reserva hecha por un usuario
    """
    if not usuario:
        print("Tenes que iniciar sesion")
        return

    print(f"\n-- Reservas de {usuario} --")
    reservas_usuario = []
    for r in reservas:
        if r["usuario"] == usuario:
            reservas_usuario.append(r)
    
    if not reservas_usuario:
        print("No tenes reservas para cancelar")
        return
    
    for r in reservas_usuario:
        print(f"ID: {r['id']} | Vuelo: {r['vuelo']} | Asientos: {r['asientos']}")
    
    id_reserva = input("\nIngrese el ID de la reserva a cancelar: ").strip()
    
    reserva_encontrada = None
    for r in reservas:
        if str(r["id"]) == str(id_reserva) and r["usuario"] == usuario:
            reserva_encontrada = r
            break
    
    if not reserva_encontrada:
        print("Reserva no encontrada o no es tuyo")
        return
    
    vuelo = get_vuelo_safe(reserva_encontrada.get("vuelo"))
    if not vuelo:
        print("El vuelo asociado a la reserva no existe")
        return
    
    matriz = vuelo.get("matriz")
    if not matriz:
        print("El vuelo no tiene matriz para liberar asientos")
        return
    
    liberados = 0
    letras = [chr(ord('A') + i for i in range(len(matriz)))]
    for etiqueta in reserva_encontrada.get("asientos", []):
        if not etiqueta or len(etiqueta) < 2:
            continue
        fila_letra = etiqueta[0].upper()
        num_txt = etiqueta[1:]
        if not num_txt.isdigit():
            continue
        f = ord(fila_letra) - ord('A')
        c = int(num_txt) - 1
        if 0 <= f < len(matriz) and 0 <= c < len(matriz[0]):
            matriz[f][c] = 0
            liberados += 1
    
    if "asientos" in vuelo:
        cant_devolver = reserva_encontrada.get("cant", liberados)
        vuelo["asientos"] = vuelo["asientos"] + cant_devolver
    
    reservas.remove(reserva_encontrada)
    save_vuelos()
    
    print(f"Reserva cancelada y {liberados} asientos devueltos")


#TODO: Hacer historial de reservas con json, tambien cargar reservas con JSON
#TODO: Crear un historial de reservas por usuario 
#TODO: historial de reservas mas ordenada
#TODO: estadisticas con lambda > calcular total el total de los asientos, reservados
