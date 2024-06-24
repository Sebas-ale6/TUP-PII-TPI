# Importar módulos
from agricultura import Agricultura
from combate import Combate
from jugador import Jugador
from mineria import Mineria

def mostrar_menu():
    print("Seleccione una opción:")
    print("1. Realizar actividad de agricultura")
    print("2. Realizar actividad de minería")
    print("3. Iniciar combate")
    print("4. Mostrar estado del jugador")
    print("5. Salir")

def menu_agricultura(agricultura):
    print("Actividades de Agricultura:")
    print("1. Trabajar en el campo")
    print("2. Alimentar animales")
    print("3. Talar árboles")
    print("4. Cultivar plantas")
    print("5. Volver al menú principal")
    opcion = input("Seleccione una actividad: ")
    
    if opcion == '1':
        print(agricultura.trabajar())
    elif opcion == '2':
        print(agricultura.alimentar_animales())
    elif opcion == '3':
        print(agricultura.talar_arboles())
    elif opcion == '4':
        print(agricultura.cultivar())
    elif opcion == '5':
        return
    else:
        print("Opción no válida")

def menu_mineria(mineria):
    print("Actividades de Minería:")
    print("1. Picar minerales")
    print("2. Explorar cuevas")
    print("3. Recoger minerales")
    print("4. Volver al menú principal")
    opcion = input("Seleccione una actividad: ")

    if opcion == '1':
        print(mineria.picar())
    elif opcion == '2':
        print(mineria.explorar_cuevas())
    elif opcion == '3':
        print(mineria.recoger_minerales())
    elif opcion == '4':
        return
    else:
        print("Opción no válida")

def main():
    # Crear instancias de clases
    jugador = Jugador(nombre="Juan")
    agricultura = Agricultura(jugador=jugador)
    mineria = Mineria(jugador=jugador)
    combate = Combate(jugador=jugador)

    while True:
        mostrar_menu()
        opcion = input("Seleccione una opción: ")

        if opcion == '1':
            menu_agricultura(agricultura)
        elif opcion == '2':
            menu_mineria(mineria)
        elif opcion == '3':
            combate.iniciar_combate()
        elif opcion == '4':
            print(f"Jugador: {jugador.nombre}, Vida: {jugador.vida}, Habilidades: {jugador.habilidades}")
        elif opcion == '5':
            print("Saliendo del programa...")
            break
        else:
            print("Opción no válida")

# Llamada directa a la función main
main()
