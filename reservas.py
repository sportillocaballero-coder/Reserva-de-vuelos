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
    letras = [chr(ord('A') + i) for i in range(filas)] #chr convierte numero en caracter y ord caracter en numero? revisar despues 
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

####buscamos el vuelo id ####
def get_vuelo_safe(vid):
    try:
        from vuelos import vuelos  # usa la lista actual
    except Exception:
        return None
    for v in vuelos:
        if str(v.get("id")) == str(vid):
            return v
    return None


    ##Cancela una reserva y libera los asientos en la matriz del vuelo.
    ###### Usa get_vuelo_safe() para recuperar el vuelo.
def cancelarReserva(id_reserva: str):
    
    try:
        r = next(r for r in reservas if r.get("id") == id_reserva)

        estado = r.get("estado", "pendiente")
        if estado == "pagada":
            print("No se puede cancelar una reserva ya pagada.")
            return

        vuelo = get_vuelo_safe(r.get("vuelo"))
        if not vuelo:
            print("El vuelo asociado a la reserva no existe.")
            return

        matriz = vuelo.get("matriz")
        if not matriz:
            print("El vuelo no tiene matriz para liberar asientos.")
            return

        def _parse_asiento(etq: str):
            if not etq or len(etq) < 2:
                return None
            fila_letra, num_txt = etq[0].upper(), etq[1:]
            if not num_txt.isdigit():
                return None
            f = ord(fila_letra) - ord('A')
            c = int(num_txt) - 1
            if 0 <= f < len(matriz) and 0 <= c < len(matriz[0]):
                return f, c
            return None

        liberados = 0
        for etiqueta in r.get("asientos", []):
            idx = _parse_asiento(etiqueta)
            if idx:
                f, c = idx
                matriz[f][c] = 0
                liberados += 1

        if "asientos" in vuelo and isinstance(vuelo["asientos"], int):
            try:
                vuelo["asientos"] += int(r.get("cant", liberados))
            except Exception:
                vuelo["asientos"] += liberados

        reservas.remove(r)
        print("Reserva cancelada y asientos devueltos.")
    except StopIteration:
        print("No existe una reserva con ese ID.")
    except Exception as e:
        print("Error al cancelar la reserva:", e)



    ##funncion pagar reserva .
    
def pagarReserva(id_reserva: str):

    try:
        r = next(r for r in reservas if r["id"] == id_reserva)
        if "estado" not in r:
            r["estado"] = "pendiente"
        if r.get("estado") == "pagada":
            print("La reserva ya está pagada.")
            return
        if r.get("estado") != "pendiente":
            print(f"No se puede pagar una reserva en estado '{r.get('estado')}'.")
            return

        actualizadas = pagar_reserva(reservas, id_reserva)
        reservas[:] = actualizadas
        print("Reserva pagada correctamente.")
    except StopIteration:
        print("No existe una reserva con ese ID.")
    except Exception as e:
        print("Error al pagar la reserva:", e)



#TODO: permitir cancelar reserva y devolver asientos al vuelo
#TODO: permitir pagar reserva (cambiar el estado a "pagada")##### (EN PROCESO)#######
#TODO: historial de reservas mas ordenada
#TODO: estadisticas con lambda > calcular total el total de los asientos, reservados

#TODO: usar listas por comprension para:
#- obtener todas las reservas de un usuario
#- calcular el total de asientos reservados con sum()
#- obtener todos los IDs de vuelos reservados