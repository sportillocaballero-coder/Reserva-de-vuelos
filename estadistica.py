#TODO: hacer esqueleto de estadistica.py

"""Funciones: 
-vueloCaro()
-vueloBarato()
-vueloMasReservado()
-totalAsientos()

"""
def mostrar_estadisticas(vuelos):
    if not vuelos:
        print("No hay vuelos cargados para mostrar estadísticas.")
        return
"""
    stats = obtener_estadisticas(vuelos)
    if not stats:
        print("No hay vuelos cargados para mostrar estadísticas.")
    return

    print("
=== ESTADÍSTICAS DE VUELOS ===")
mc = stats.get('mas_caro')
mb = stats.get('mas_barato')
mr = stats.get('mas_reservado')
print(f"Vuelo más caro: ID {mc['id']} | {mc['origen']} -> {mc['destino']} | Precio: ${mc['precio']}")
print(f"Vuelo más barato: ID {mb['id']} | {mb['origen']} -> {mb['destino']} | Precio: ${mb['precio']}")
print(f"Vuelo más reservado: ID {mr['id']} | {mr['origen']} -> {mr['destino']} | Reservados: {mr['reservados']}")
print(f"Precio promedio de vuelos: ${stats.get('precio_promedio'):.2f}")


"""

# Vuelo más caro
mas_caro = max(vuelos, key=lambda v: v['precio'])

# Vuelo más barato
mas_barato = min(vuelos, key=lambda v: v['precio'])

# Vuelo más reservado (menos asientos disponibles)
mas_reservado = min(vuelos, key=lambda v: v['asientos'])

print("\n=== ESTADÍSTICAS DE VUELOS ===")
print(f"Vuelo más caro: ID {mas_caro['id']} | {mas_caro['origen']} -> {mas_caro['destino']} | Precio: ${mas_caro['precio']}")
print(f"Vuelo más barato: ID {mas_barato['id']} | {mas_barato['origen']} -> {mas_barato['destino']} | Precio: ${mas_barato['precio']}")
print(f"Vuelo más reservado: ID {mas_reservado['id']} | {mas_reservado['origen']} -> {mas_reservado['destino']} | Asientos restantes: {mas_reservado['asientos']}")



# def contar_reservados_en_vuelo(v):




def obtener_estadisticas(vuelos, usuarios=None, reservas=None):
    """
    Devuelve un diccionario con estadísticas calculadas a partir de la lista `vuelos`.
    Claves devueltas:
    - mas_caro: dict del vuelo más caro
    - mas_barato: dict del vuelo más barato
    - mas_reservado: dict del vuelo con más asientos reservados (incluye campo 'reservados')
    - precio_promedio: float
    - total_vuelos: int
    - usuario_mas_activo: id/usuario más activo según `reservas` (si se pasa)
    """
    if not vuelos:
        return {}


# asegurar que los vuelos tengan las claves mínimas
vuelos_validos = [v for v in vuelos if isinstance(v, dict) and 'precio' in v and 'id' in v]
if not vuelos_validos:
    return {}


# precio promedio
precios = [float(v['precio']) for v in vuelos_validos]
precio_promedio = sum(precios) / len(precios)

mas_caro = max(vuelos_validos, key=lambda v: float(v['precio']))
mas_barato = min(vuelos_validos, key=lambda v: float(v['precio']))


# calcular reservados por vuelo
for v in vuelos_validos:
    v['_reservados_calc'] = contar_reservados_en_vuelo(v)


mas_reservado_v = max(vuelos_validos, key=lambda v: v.get('_reservados_calc', 0))


resultado = {
'mas_caro': mas_caro,
'mas_barato': mas_barato,
'mas_reservado': {
'id': mas_reservado_v['id'],
'origen': mas_reservado_v.get('origen', ''),
'destino': mas_reservado_v.get('destino', ''),
'reservados': mas_reservado_v.get('_reservados_calc', 0)
},
'precio_promedio': precio_promedio,
'total_vuelos': len(vuelos_validos)
}


#TODO: estadisticas con lambda > obtener vuelo mas caro
#TODO: estadisticas con lambda > obtener vuelo mas barato
#TODO: estadisticas con lambda > obtener vuelo mas reservado

#TODO: usar listas por comprension para:
#- obtener lista de precios de vuelos
#- obtener todos los usuarios que hicieron reservas
#- obtener todos los vuelos reservados por un usuario especifico
#- simplificar calculos de estadisticas (vuelo mas caro, mas barato, etc.)

precios = [v['precio'] for v in vuelos]
promedio = sum(precios) / len(precios)
print(f"Precio promedio de vuelos: ${promedio:.2f}")