from jugador import Jugador
import random

class Combate:
    def __init__(self, jugador: Jugador):
        self.jugador = jugador

    def iniciar_combate(self):
        resultado_combate = random.random()  
        if resultado_combate < 0.5:  # 50% de probabilidad de ganar
            experiencia_ganada = 25
            self.jugador.ganar_experiencia("combate", experiencia_ganada)
        else:
            vida_perdida = 20
            self.jugador.vida = max(self.jugador.vida - vida_perdida, 0)
            print(f"Perdiste {vida_perdida} puntos de vida. Vida actual: {self.jugador.vida}")