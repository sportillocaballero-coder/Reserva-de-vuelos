from vuelos import vuelos
from reservas import vecesReservado

#TODO: HAcer estadisticas mas atractivas
def vueloCaro():
    print("El vuelo mas caro es: ")
    vueloMasCaro = max(vuelos, key=lambda vuelo: vuelo['precio'])
    return vueloMasCaro

def vueloBarato():
    print("El vuelo mas barato es: ")
    vueloMasBarato = min(vuelos, key=lambda vuelo: vuelo['precio'])
    return vueloMasBarato

def vueloMasReservado():
    print("El vuelo mas reservado es: ")
    reservaMasAlta = max(vecesReservado, key=lambda reserva: reserva['contador'])
    return reservaMasAlta

def totalAsientos():
    print("Cantidad total de asientos disponibles: ")
    total = sum([vuelo['asientos'] for vuelo in vuelos])
    return total

def estadisticas():
    c = True
    while c:
        print("1. Vuelo Mas Caro")
        print("2. Vuelo Mas Barato")
        print("3. Vuelo Mas Reservados")
        print("4. Total de Asientos") 
        print("5. Salir")
        opcion = input("Seleccione una opcion: ").strip()
        if opcion == "1":
            print(vueloCaro())
        elif opcion == "2":
            print(vueloBarato())
        elif opcion == "3":
            print(vueloMasReservado())
        elif opcion == "4":
            print(totalAsientos())
        elif opcion == "5":
            c = False
        else:
            print("Opción inválida, intente nuevamente porfavor.")