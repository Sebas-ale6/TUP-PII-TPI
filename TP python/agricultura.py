from jugador import Jugador

class Agricultura:
    def __init__(self, jugador: Jugador):
        self.jugador = jugador

    def trabajar(self):
        experiencia = 25
        self.jugador.ganar_experiencia("agricultura", experiencia)
        return {"tipo": "agricultura", "valor": experiencia, "descripcion": "Has trabajado en el campo"}

    def alimentar_animales(self):
        experiencia = 25
        self.jugador.ganar_experiencia("agricultura", experiencia)
        return {"tipo": "agricultura", "valor": experiencia, "descripcion": "Has alimentado a los animales"}

    def talar_arboles(self):
        experiencia = 25
        self.jugador.ganar_experiencia("agricultura", experiencia)
        return {"tipo": "agricultura", "valor": experiencia, "descripcion": "Has talado arboles"}

    def cultivar(self):
        experiencia = 25
        self.jugador.ganar_experiencia("agricultura", experiencia)
        return {"tipo": "agricultura", "valor": experiencia, "descripcion": "Has cultivado las plantas"}