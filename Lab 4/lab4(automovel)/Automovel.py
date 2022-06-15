from Motor import *

class Automovel():
    def __init__(self):
        self.motor = None
        self.velocidade_maxima = None
        self.massa = None
        self.aceleracao_freio = None
        self.velocidade = 0
        self.direcao = 0

    def mostrarVelocidade(self):
        print(f'minha velocidade é {self.velocidade}')

    def mostrarDirecao(self):
        print(f'minha direcao é {self.direcao}')


class Carro(Automovel):
    def __init__(self):
        super().__init__()
        self.velocidade_maxima = 150
        self.massa = 2000
        self.aceleracao_freio = 2


class Caminhao(Automovel):
    def __init__(self):
        super().__init__()
        self.velocidade_maxima = 80
        self.massa = 5000
        self.aceleracao_freio = 1.5


class Moto(Automovel):
    def __init__(self):
        super().__init__()
        self.velocidade_maxima = 200
        self.massa = 500
        self.aceleracao_freio = 4