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

def vueloCaro():
    print("El vuelo mas caro es: ")
    vuelos = leerReservasJson("vuelos.json")
    vueloMasCaro = max(vuelos, key=lambda vuelo: vuelo['precio'])
    return vueloMasCaro

def vueloBarato():
    print("El vuelo mas barato es: ")
    vuelos = leerReservasJson("vuelos.json")
    vueloMasBarato = min(vuelos, key=lambda vuelo: vuelo['precio'])
    return vueloMasBarato

def totalAsientos():
    vuelos = leerReservasJson("vuelos.json")
    print("Cantidad total de asientos disponibles: ")
    total = sum([vuelo['asientos'] for vuelo in vuelos])
    return total

def estadisticas():
    c = True
    while c:
        print("1. Vuelo Mas Caro")
        print("2. Vuelo Mas Barato")
        print("3. Total de Asientos") 
        print("4. Salir")
        opcion = input("Seleccione una opcion: ").strip()
        if opcion == "1":
            print(vueloCaro())
        elif opcion == "2":
            print(vueloBarato())
        elif opcion == "3":
            print(totalAsientos())
        elif opcion == "4":
            c = False
        else:
            print("Opción inválida, intente nuevamente porfavor.")