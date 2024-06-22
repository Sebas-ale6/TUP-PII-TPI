from experiencia import Experiencia

class Mineria:
    def __init__(self):
        self.experiencia_generada = 0

    def picar(self):
        experiencia_generada = 15
        return Experiencia("Minería", experiencia_generada, "Has picado un mineral.")