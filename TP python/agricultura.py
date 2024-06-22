from experiencia import Experiencia

class Agricultura:
    def __init__(self):
        self.experiencia_generada = 0

    def trabajar(self):
        experiencia_generada = 10
        return Experiencia("Agricultura", experiencia_generada, "Has trabajado en el campo")