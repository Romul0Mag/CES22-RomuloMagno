import abc
from Bolo import *

class Builder():
    __metaclass__ = abc.ABCMeta

    @abc.abstractmethod
    def reset(self):
        pass

    @abc.abstractmethod
    def setSabor(self, sabor):
        pass

    @abc.abstractmethod
    def getResult(self):
        pass


class AniversarioBuilder(Builder):

    def __init__(self):
        self.bolo_aniversario = BoloAniversario()

    def reset(self):
        self.bolo_aniversario.sabor = None

    def setSabor(self, sabor):
        self.bolo_aniversario.sabor = sabor

    def getResult(self):
        return self.bolo_aniversario


class InformalBuilder(Builder):

    def __init__(self):
        self.bolo_informal = BoloInformal()

    def reset(self):
        self.bolo_informal.sabor = None

    def setSabor(self, sabor):
        self.bolo_informal.sabor = sabor

    def getResult(self):
        return self.bolo_informal

class CasamentoBuilder(Builder):

    def __init__(self):
        self.bolo_casamento = BoloCasamento()

    def reset(self):
        self.bolo_casamento.sabor = None

    def setSabor(self, sabor):
        self.bolo_casamento.sabor = sabor

    def getResult(self):
        return self.bolo_casamento