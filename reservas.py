from vuelos import vuelos, save_vuelos   #Acceso a lista de vuelos y persistencia
import random
import os
import json

reservas = []

VUELOS_DIR = os.path.join(os.path.dirname(__file__), "datos")
VUELOS_FILE = os.path.join(VUELOS_DIR, "reservas.json")

def archivoReserva(lista):
    try:
        if not os.path.exists(VUELOS_DIR):
            os.makedirs(VUELOS_DIR)
        with open(VUELOS_FILE, 'w', encoding='utf-8') as f:
            json.dump(lista, f, indent=4, ensure_ascii=False)
        return True
    except Exception as e:
        print(f"Error al guardar vuelos: {e}")
        return False
    
def leerReservasJson():
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

    nuevaReserva = leerReservasJson()
    nuevaReserva.append(reserva)
    archivoReserva(nuevaReserva)

    save_vuelos()

    print(f"Reserva creada( Vuelo:{reserva['vuelo']} || Asientos: {reserva['asientos']} )")

def verReserva(usuario):
    """
    Objetivo: Mostrar todas las reservas realizadas por el usuario.
    Parametros:
      - usuario (str): Usuario logueado.
    Retorna: Nada.
    """
    reservasLoad = leerReservasJson()
    reservas_filtradas = list(filter(lambda reserva: reserva['usuario'] == usuario, reservasLoad))
    print(f"| RESERVAS ENCONTRADAS PARA EL USUARIO: {usuario} |")
    if not reservas_filtradas:
        print("| No se encontraron reservas activas para este usuario. |")
        return False
    else:
        for reserva in reservas_filtradas:
            # Convierte la lista de asientos a una cadena legible (ej: 'A5, D1')
            asientos_str = ", ".join(reserva['asientos'])

            print(f"| ID Reserva: {reserva['id']:<10} | Vuelo: {reserva['vuelo']:<8} | Estado: {reserva['estado'].upper():<10} |")
            print(f"| Asientos: {asientos_str:<20} | Cantidad: {reserva['cant']} |")
            print("-" * 50) # Separador entre reservas
        return reservas_filtradas
    
def obtener_coordenadas(asiento_str):
    """Convierte la notación alfanumérica del asiento a índices [fila, columna] (base 0)."""
    
    fila_letra = asiento_str[0]
    columna_num_str = asiento_str[1:]
    
    # FILA: 'A' es 0, 'B' es 1, etc.
    fila_idx = ord(fila_letra.upper()) - ord('A')
    
    columna_idx = int(columna_num_str) - 1
    
    return fila_idx, columna_idx

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

    # 1. Mostrar reservas y obtener la lista filtrada de reservas del usuario
    reservasUsuario = verReserva(usuario) 
    
    if not reservasUsuario:
        print("No tenes reservas para cancelar")
        return

    # 2. Pedir ID de reserva y buscar el objeto reserva
    id_reserva = input("\nIngrese el ID de la reserva a cancelar: ").strip()
    
    reserva_encontrada_list = list(filter(lambda r: str(r['id']) == id_reserva, reservasUsuario))
    
    if not reserva_encontrada_list:
        print(f"ID de reserva {id_reserva} no encontrado en tus reservas.")
        return

    reserva_a_cancelar = reserva_encontrada_list[0]
    
    vuelo_id = reserva_a_cancelar['vuelo']
    asientos_a_liberar = reserva_a_cancelar['asientos']
    cantidad_asientos = reserva_a_cancelar['cant']

    # 3. Buscar el objeto VUELO en la lista global `vuelos`
    vuelo = None
    for v in vuelos:
        if str(v["id"]) == str(vuelo_id):
            vuelo = v
            break
            
    if not vuelo:
        print(f"Error: El vuelo {vuelo_id} asociado a la reserva no fue encontrado.")
        return

    # 4. Actualizar la MATRIZ del vuelo
    matriz = vuelo.get("matriz")
    if matriz:
        for asiento_str in asientos_a_liberar:
            try:
                fila_idx, col_idx = obtener_coordenadas(asiento_str)
                
                if 0 <= fila_idx < len(matriz) and 0 <= col_idx < len(matriz[0]):
                    matriz[fila_idx][col_idx] = 0
                    print(f"Asiento {asiento_str} liberado en la matriz del vuelo {vuelo_id}.")
                else:
                    print(f"Error interno: Asiento {asiento_str} fuera de los límites de la matriz.")
                    
            except Exception:
                print(f"Error al procesar el formato del asiento {asiento_str}.")

    # 5. Actualizar el contador de asientos disponibles del vuelo
    if "asientos" in vuelo:
        vuelo["asientos"] += cantidad_asientos
        print(f"Total de asientos disponibles en el vuelo {vuelo_id} aumentado en {cantidad_asientos}.")
        
    # 6. Eliminar la reserva de la lista global y guardar el archivo
    
    todas_las_reservas = leerReservasJson()
    
    # Crear una nueva lista excluyendo la reserva a cancelar
    nueva_lista_reservas = [r for r in todas_las_reservas if str(r['id']) != id_reserva]
    
    if len(nueva_lista_reservas) == len(todas_las_reservas):
        print(" Error: No se pudo eliminar la reserva del registro.")
    else:
        # Guardar la lista de reservas sin la reserva cancelada
        archivoReserva(nueva_lista_reservas)
        print(f"\n Reserva {id_reserva} cancelada y eliminada del registro.")
        
    save_vuelos()
    
    print("El estado de los vuelos ha sido actualizado.")
    

