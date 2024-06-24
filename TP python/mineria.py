from jugador import Jugador

class Mineria:
    def _init_(self, jugador: Jugador):
        self.jugador = jugador

    def picar(self):
        experiencia = 35
        self.jugador.ganar_experiencia("mineria", experiencia)
        return {"tipo": "minería", "valor": experiencia, "descripcion": "Has picado minerales en la mina"}

    def explorar_cuevas(self):
        experiencia = 30
        self.jugador.ganar_experiencia("mineria", experiencia)
        return {"tipo": "minería", "valor": experiencia, "descripcion": "Has explorado las minas"}

    def recoger_minerales(self):
        experiencia = 35
        self.jugador.ganar_experiencia("mineria", experiencia)
        return {"tipo": "minería", "valor": experiencia, "descripcion": "Has recogido el mineral"}
