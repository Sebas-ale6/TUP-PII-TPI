class Jugador:
    def __init__(self, nombre: str, vida: int = 100):
        self.nombre = nombre
        self.vida = vida
        self.habilidades = {"agricultura": 0, "mineria": 0, "combate": 0}

    def ganar_experiencia(self, tipo: str, valor: int):
        if tipo in self.habilidades:
            self.habilidades[tipo] = self.habilidades[tipo] + valor
            print(f"Ganaste {valor} puntos de experiencia en {tipo}. Nivel de {tipo} actual: {self.habilidades[tipo]}")
        
