from experiencia import Experiencia

class Combate:
    def __init__(self):
        self.experiencia_generada = 0

    def luchar(self):
        experiencia_generada = 20
        return Experiencia("Combate", experiencia_generada, "Has derrotado a un enemigo")