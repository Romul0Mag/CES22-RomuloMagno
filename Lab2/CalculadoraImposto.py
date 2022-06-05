from Produto import Produto
import abc


class CalculadoraImposto():
    __metaclass__ = abc.ABCMeta

    def __init__(self):
        self.a = 0.2
        self.b = 0.9

    @abc.abstractmethod
    def calcularImposto(self, produto):
        pass

class ImpostoLivroBR2022(CalculadoraImposto):

    def calcularImposto(self, produto):
        return self.a*(produto.preco_venda - produto.preco_compra) + self.b*produto.genero.constante_imposto