import json
import os

VUELOS_DIR = os.path.join(os.path.dirname(__file__), "datos")

def leerReservasJson(archivo):
    VUELOS_FILE = os.path.join(VUELOS_DIR, archivo)
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

def vueloCaro(vuelos):
    """
    Objetivo:Encuentra el vuelo mas caro
    Parametros:
    - vuelos (list): Lista de vuelos
    Retorna: dict - El vuelo mas caro 
    """
    if not vuelos:
        print("\n No hay vuelos registrados")
        return None
    
    vueloMasCaro = max(vuelos, key=lambda vuelo: vuelo['precio'])
    
    print("\n" + "="*57)
    print(" VUELO MAS CARO")
    print("="*57)
    print(f" ID: {vueloMasCaro['id']}")
    print(f" Origen: {vueloMasCaro['origen']}")
    print(f" Destino: {vueloMasCaro['destino']}")
    print(f" Fecha: {vueloMasCaro['fecha']}")
    print(f" Precio: ${vueloMasCaro['precio']}")
    print(f" Asientos Disponibles: {vueloMasCaro['asientos']}")
    print("="*57)
    return vueloMasCaro

def vueloBarato(vuelos):
    """
    Objetivo: Encuentra el vuelo mas barato
    Parametros:
    - vuelos (list): Lista de vuelos
    Retorna: dict - El vuelo mas barato
    """
    if not vuelos:
        print("\n No hay vuelos registrados")
        return None
    
    vueloMasBarato = min(vuelos, key=lambda vuelo: vuelo['precio'])
    
    print("\n" + "="*57)
    print(" VUELO MAS BARATO")
    print("="*57)
    print(f" ID: {vueloMasBarato['id']}")
    print(f" Origen: {vueloMasBarato['origen']}")
    print(f" Destino: {vueloMasBarato['destino']}")
    print(f" Fecha: {vueloMasBarato['fecha']}")
    print(f" Precio: ${vueloMasBarato['precio']}")
    print(f" Asientos Disponibles: {vueloMasBarato['asientos']}")
    print("="*57)
    return vueloMasBarato

def totalAsientos(vuelos):
    """
    Objetivo: Calcula el total de asientos disponibles en toods los vuelos 
    Parametros:
    - vuelos (list): Lista de vuelos
    Retorna: int - El total de asiento
    """
    if not vuelos:
        print("\n No hay vuelos registrados")
        return 0
    
    total = sum([vuelo['asientos'] for vuelo in vuelos])
    
    print("\n" + "="*57)
    print(" TOTAL DE ASIENTOS DISPONIBLES")
    print("="*57)
    print(f" Asientos Totales: {total} asientos")
    print(f" Vuelos Analizados: {len(vuelos)} vuelos")
    print(f" Promedio por Vuelo: {round(total/len(vuelos), 2)} asientos")
    print("="*57)
    return total

def totalVuelos(vuelos):
    """
    Objetivo: Cuenta el total de los vuelos creados en el sistema 
    Parametros:
    - vuelos (list): Lista de vuelos
    Retorna: int - Cantidad de vuelos
    """
    total = len(vuelos)
    
    print("\n" + "="*57)
    print(" TOTAL DE VUELOS CREADOS")
    print("="*57)
    print(f" Total de Vuelos: {total} vuelos")
    print("="*57)
    return total

def promedioPrecios(vuelos):
    """
    Objetivo: Calcula el precio promedio de todos los vuelos creados
    Parametros:
    - vuelos (list): Lista de vuelos
    Retorna: float - Precio promedio
    """
    if not vuelos:
        print("\n No hay vuelos registrados")
        return 0
    
    precios = [vuelo['precio'] for vuelo in vuelos]
    promedio = sum(precios) / len(vuelos)
    precio_min = min(precios)
    precio_max = max(precios)
    
    print("\n" + "="*57)
    print(" PRECIO PROMEDIO DE VUELOS")
    print("="*57)
    print(f" Precio Promedio: ${round(promedio, 2)}")
    print(f" Precio Minimo: ${precio_min}")
    print(f" Precio Maximo: ${precio_max}")
    print(f" Vuelos Analizados: {len(vuelos)} vuelos")
    print("="*57)
    return round(promedio, 2)

def totalIngresos(vuelos, reservas):
    """
    Objetivo: Calcula el total de ingresos generados por todas las reservas hecas
    Parametros:
    - vuelos (list): Lista de vuelos
    - reservas (list): Lista de reservas
    Retorna: float - Total de ingresos
    """
    if not vuelos or not reservas:
        print("\n No hay suficientes datos para calcular ingresos")
        return 0
    
    # Crear diccionario de precios por vuelo para búsqueda rápida
    precios_vuelos = {str(vuelo['id']): vuelo['precio'] for vuelo in vuelos}
    
    total = 0
    reservas_validas = 0
    
    for reserva in reservas:
        vuelo_id = str(reserva.get('vuelo', ''))
        cantidad = reserva.get('cant', 0)
        
        if vuelo_id in precios_vuelos:
            precio = precios_vuelos[vuelo_id]
            ingreso = precio * cantidad
            total += ingreso
            reservas_validas += 1
    
    print("\n" + "="*57)
    print(" TOTAL DE INGRESOS GENERADOS")
    print("="*57)
    print(f" Ingresos Totales: ${round(total, 2)}")
    print(f" Reservas Contabilizadas: {reservas_validas} reservas")
    print(f" Total de Reservas: {len(reservas)} reservas")
    if reservas_validas > 0:
        print(f" Ingreso Promedio por Reserva: ${round(total/reservas_validas, 2)}")
    print("="*57)
    return round(total, 2)

def usuarioMasReservas(reservas):
    """
    Objetivo: Encontrar usuario con mas reservas
    Parametros:
    - reservas (list): Lista de reservas
    Retorna: str - Usuario con mas reservas
    """
    if not reservas:
        print("\n No hay reservas registradas")
        return None
    
    usuarios = {}
    for reserva in reservas:
        usuario = reserva.get('usuario', 'Desconocido')
        usuarios[usuario] = usuarios.get(usuario, 0) + 1
    
    usuario_top = max(usuarios.items(), key=lambda x: x[1])
    
    print("\n" + "="*57)
    print(" USUARIO CON MAS RESERVAS")
    print("="*57)
    print(f" Usuario: {usuario_top[0]}")
    print(f" Cantidad de Reservas: {usuario_top[1]} reservas")
    print(f" Total de Usuarios: {len(usuarios)} usuarios")
    print("="*57)
    return f"{usuario_top[0]} con {usuario_top[1]} reservas"

def totalReservasActivas(reservas):
    """
    Objetivo: Contar total de reservas activas
    Parametros:
    - reservas (list): Lista de reservas
    Retorna: int - Cantidad de reservas
    """
    total = len(reservas)
    
    print("\n" + "="*57)
    print(" TOTAL DE RESERVAS ACTIVAS")
    print("="*57)
    print(f" Total de Reservas: {total} reservas")
    print("="*57)
    return total

def vueloMasReservado(reservas):
    """
    Objetivo: Encontrar vuelo mas reservado
    Parametros:
    - reservas (list): Lista de reservas
    Retorna: str - Vuelo mas reservado
    """
    if not reservas:
        print("\n No hay reservas registradas")
        return None
    
    vuelos_reservados = {}
    for reserva in reservas:
        vuelo_id = reserva.get('vuelo', 'Desconocido')
        vuelos_reservados[vuelo_id] = vuelos_reservados.get(vuelo_id, 0) + 1
    
    vuelo_top = max(vuelos_reservados.items(), key=lambda x: x[1])
    
    print("\n" + "="*57)
    print(" VUELO MAS RESERVADO")
    print("="*57)
    print(f" ID del Vuelo: {vuelo_top[0]}")
    print(f" Cantidad de Reservas: {vuelo_top[1]} reservas")
    print(f" Total de Vuelos Reservados: {len(vuelos_reservados)} vuelos")
    print("="*57)
    return f"Vuelo ID {vuelo_top[0]} con {vuelo_top[1]} reservas"

def destinoMasPopular(vuelos):
    """
    Objetivo: Encuentra el destino mas elejido por los usuarios
    Parametros:
    - vuelos (list): Lista de vuelos
    Retorna: str - Destino mas popular
    """
    if not vuelos:
        print("\n No hay vuelos registrados")
        return None
    
    destinos = [vuelo['destino'] for vuelo in vuelos]
    destino_popular = max(set(destinos), key=destinos.count)
    cantidad = destinos.count(destino_popular)
    destinos_unicos = len(set(destinos))
    
    print("\n" + "="*57)
    print(" DESTINO MAS POPULAR")
    print("="*57)
    print(f" Destino: {destino_popular}")
    print(f" Cantidad de Vuelos: {cantidad} vuelos")
    print(f" Total de Destinos: {destinos_unicos} destinos")
    print("="*57)
    return f"{destino_popular} con {cantidad} vuelos"

def verTodasEstadisticas():
    """
    Objetivo: Muestra el resumen completo de estadisticas
    Parametros: Nada
    Retorna: Nada
    """
    vuelos = leerReservasJson("vuelos.json")
    reservas = leerReservasJson("reservas.json")
    
    print("\n" + "="*57)
    print(" RESUMEN COMPLETO DE ESTADISTICAS")
    print("="*57)
    
    print("\n--- ESTADISTICAS DE VUELOS ---")
    vueloCaro(vuelos)
    vueloBarato(vuelos)
    totalVuelos(vuelos)
    promedioPrecios(vuelos)
    destinoMasPopular(vuelos)
    totalAsientos(vuelos)
    
    print("\n--- ESTADISTICAS DE RESERVAS ---")
    totalReservasActivas(reservas)
    vueloMasReservado(reservas)
    usuarioMasReservas(reservas)
    
    print("\n--- ESTADISTICAS FINANCIERAS ---")
    totalIngresos(vuelos, reservas)
    
    print("\n" + "="*57)
    print(" FIN DEL REPORTE")
    print("="*57)

def estadisticas():
    """
    Objetivo: Menu principal de estadisticas
    Parametros: Nada
    Retorna: Nada
    """
    bandera = True
    while bandera:
        vuelos = leerReservasJson("vuelos.json")
        reservas = leerReservasJson("reservas.json")
        
        print("\n=== ESTADISTICAS DEL SISTEMA ===")
        print("1. Vuelo Mas Caro")
        print("2. Vuelo Mas Barato")
        print("3. Total de Asientos Disponibles")
        print("4. Total de Vuelos Creados")
        print("5. Precio Promedio de Vuelos")
        print("6. Usuario con Mas Reservas")
        print("7. Total de Reservas Activas")
        print("8. Vuelo Mas Reservado")
        print("9. Destino Mas Popular")
        print("10. Total de Ingresos Generados")
        print("11. Ver todas las estadisticas")
        print("12. Salir")
        opcion = input("Seleccione una opcion: ").strip()
        
        if opcion == "1":
            vueloCaro(vuelos)
        elif opcion == "2":
            vueloBarato(vuelos)
        elif opcion == "3":
            totalAsientos(vuelos)
        elif opcion == "4":
            totalVuelos(vuelos)
        elif opcion == "5":
            promedioPrecios(vuelos)
        elif opcion == "6":
            usuarioMasReservas(reservas)
        elif opcion == "7":
            totalReservasActivas(reservas)
        elif opcion == "8":
            vueloMasReservado(reservas)
        elif opcion == "9":
            destinoMasPopular(vuelos)
        elif opcion == "10":
            totalIngresos(vuelos, reservas)
        elif opcion == "11":
            verTodasEstadisticas()
        elif opcion == "12":
            bandera = False
        else:
            print("Opción inválida, intente nuevamente porfavor.")