from agricultura import Agricultura
from combate import Combate
from jugador import Jugador
from mineria import Mineria
import os  # Importa el módulo os para limpiar la consola

def limpiar_consola():
    os.system('cls' if os.name == 'nt' else 'clear')

def mostrar_menu():
    print("Bienvenido al juego!")
    print("Hola usuario! Soy tu personaje, puedes hacer que yo haga una variedad limitada de actividades(agricultura, mineria, combate) en las cuales ire juntando la experiencia necesaria para triunfar en nuestra aventura")
    print("y bien? Que desea hacer?: ")
    print("1. Realizar actividad de agricultura")
    print("2. Realizar actividad de minería")
    print("3. Iniciar combate")
    print("4. Mostrar estado del jugador")
    print("5. Salir")

def menu_agricultura(agricultura):
    while True:
        limpiar_consola()
        print("Actividades de Agricultura:")
        print("1. Trabajar en el campo")
        print("2. Alimentar animales")
        print("3. Talar árboles")
        print("4. Cultivar plantas")
        print("5. Volver al menú principal")
        opcion = input("Seleccione la actividad que desea realizar: ")
        
        limpiar_consola()
        if opcion == '1':
            print(agricultura.trabajar())
        elif opcion == '2':
            print(agricultura.alimentar_animales())
        elif opcion == '3':
            print(agricultura.talar_arboles())
        elif opcion == '4':
            print(agricultura.cultivar())
        elif opcion == '5':
            break
        else:
            print("Ingrese una opcion valida(1-5)")
        
        input("\nPresione Enter para volver al menú...")

def menu_mineria(mineria):
    while True:
        limpiar_consola()
        print("Actividades de Minería:")
        print("1. Picar minerales")
        print("2. Explorar cuevas")
        print("3. Recoger minerales")
        print("4. Volver al menú principal")
        opcion = input("Seleccione la actividad que desea realizar: ")
        
        limpiar_consola()
        if opcion == '1':
            print(mineria.picar())
        elif opcion == '2':
            print(mineria.explorar_cuevas())
        elif opcion == '3':
            print(mineria.recoger_minerales())
        elif opcion == '4':
            break
        else:
            print("Ingrese una opcion valida(1-4)")
        
        input("\nPresione Enter para volver al menú...")

def main():
    # Crear instancias de clases
    jugador = Jugador(nombre="Goku")
    agricultura = Agricultura(jugador=jugador)
    mineria = Mineria(jugador=jugador)
    combate = Combate(jugador=jugador)

    while True:
        limpiar_consola()  # Limpia la consola antes de mostrar el menú
        mostrar_menu()
        opcion = input("Seleccione la actividad que desea realizar: ")
        
        ########### MARTIN SUBIO ESTO ############
        if jugador.habilidades["agricultura"] >= 50 and jugador.habilidades["mineria"] >= 50 and jugador.habilidades["combate"] >= 50:      ########### MARTIN SUBIO ESTO ############
            print("GAME OVER: ganaste el juego, sos crack")
            break
        ########### MARTIN SUBIO ESTO ############
        
        if opcion == '1':
            menu_agricultura(agricultura)
        elif opcion == '2':
            menu_mineria(mineria)
        elif opcion == '3':
            limpiar_consola()
            combate.iniciar_combate()
            ########### MARTIN SUBIO ESTO ############
            if jugador.vida == 0:
                print("GAME OVER(es lo mejor que te pudo pasar, dedicate a otra cosa)")          ########### MARTIN SUBIO ESTO ############
                break
            ########### MARTIN SUBIO ESTO ############
            input("\nPresione Enter para volver al menú...")
        elif opcion == '4':
            limpiar_consola()
            print(f"Jugador: {jugador.nombre}, Vida: {jugador.vida}, Habilidades: {jugador.habilidades}")
            input("\nPresione Enter para volver al menú...")
        elif opcion == '5':
            limpiar_consola()
            print("Saliendo del juego...")
            break
        else:
            limpiar_consola()
            print("Ingrese una opcion valida(1-5)")
            input("\nPresione Enter para volver al menú...")

# Llamada directa a la función main
main()
