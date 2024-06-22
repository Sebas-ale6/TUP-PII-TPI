from experiencia import Experiencia

class Jugador:
    def __init__(self, nombre: str, vida: int = 100, habilidad_agricultura: int = 0, habilidad_mineria: int = 0, habilidad_combate: int = 0):
        self.nombre = nombre
        self.botas = []
        self.vida = vida
        self.habilidad_agricultura = habilidad_agricultura
        self.habilidad_mineria = habilidad_mineria
        self.habilidad_combate = habilidad_combate

    def experiencia_agricultura(self, experiencia: Experiencia):
        if experiencia.tipo == "Agricultura":
            self.habilidad_agricultura += experiencia.valor
        else:
            raise ValueError("La experiencia no es de tipo Agricultura")

    def experiencia_mineria(self, experiencia: Experiencia):
        if experiencia.tipo == "Minería":
            self.habilidad_mineria += experiencia.valor
        else:
            raise ValueError("La experiencia no es de tipo Minería")

    def experiencia_combate(self, experiencia: Experiencia):
        if experiencia.tipo == "Combate":
            self.habilidad_combate += experiencia.valor
        else:
            raise ValueError("La experiencia no es de tipo Combate")