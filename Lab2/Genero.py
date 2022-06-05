


class Genero():
    def __init__(self):
        self.constante_imposto = 0
        self.nome = ''

class Romance(Genero):
    def __init__(self, nome):
        super().__init__()
        self.nome = "Romance" + nome
        self.constante_imposto = 1

class Terror(Genero):
    def __init__(self, nome):
        super().__init__()
        self.nome = "Terror" + nome
        self.constante_imposto = 2

class Aventura(Genero):
    def __init__(self, nome):
        super().__init__()
        self.nome = "Aventura" + nome
        self.constante_imposto = 3

romance_cult = Romance("cult")
terror_pesado = Terror("pesado")
aventura_fantasia = Aventura("fantasia")