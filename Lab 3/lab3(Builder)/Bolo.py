

class Bolo():
    def __init__(self):
        self.estilo = None
        self.sabor = None

    def exporInfo(self):
        print(f"esse é um bolo de estilo {self.estilo} e sabor {self.sabor}")


class BoloAniversario(Bolo):
    def __init__(self):
        super().__init__()
        self.estilo = "Aniversário"


class BoloInformal(Bolo):
    def __init__(self):
        super().__init__()
        self.estilo = "Informal"


class BoloCasamento(Bolo):
    def __init__(self):
        super().__init__()
        self.estilo = "Casamento"

