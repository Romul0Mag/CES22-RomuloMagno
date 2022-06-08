

class Bolo():
    def __init__(self):
        self.estilo = None
        self.sabor = None

    def exporInfo(self):
        print(f"esse é um bolo de estilo {self.estilo} e sabor {self.sabor}")


class BoloMandioca(Bolo):
    def __init__(self):
        super().__init__()
        self.sabor = "Mandioca"



class AniversarioMandioca(BoloMandioca):
    def __init__(self):
        super().__init__()
        self.estilo = "Aniversario"


class CasamentoMandioca(BoloMandioca):
    def __init__(self):
        super().__init__()
        self.estilo = "Casamento"


class InformalMandioca(BoloMandioca):
    def __init__(self):
        super().__init__()
        self.estilo = "Informal"


class BoloCenoura(Bolo):
    def __init__(self):
        super().__init__()
        self.sabor = "Cenoura"


class AniversarioCenoura(BoloCenoura):
    def __init__(self):
        super().__init__()
        self.estilo = "Aniversario"


class CasamentoCenoura(BoloCenoura):
    def __init__(self):
        super().__init__()
        self.estilo = "Casamento"


class InformalCenoura(BoloCenoura):
    def __init__(self):
        super().__init__()
        self.estilo = "Informal"


class BoloChocolate(Bolo):
    def __init__(self):
        super().__init__()
        self.sabor = "Chocolate"


class AniversarioChocolate(BoloChocolate):
    def __init__(self):
        super().__init__()
        self.estilo = "Aniversario"


class CasamentoChocolate(BoloChocolate):
    def __init__(self):
        super().__init__()
        self.estilo = "Casamento"


class InformalChocolate(BoloChocolate):
    def __init__(self):
        super().__init__()
        self.estilo = "Informal"

