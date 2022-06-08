from Bolo import *
import abc

class FabricaBolo():
    __metaclass__ = abc.ABCMeta

    @abc.abstractmethod
    def criarBoloChocolate(self):
        pass

    @abc.abstractmethod
    def criarBoloCenoura(self):
        pass

    @abc.abstractmethod
    def criarBoloMandioca(self):
        pass


class FabricaAniversario(FabricaBolo):

     def criarBoloChocolate(self):
        return AniversarioChocolate()

     def criarBoloCenoura(self):
        return AniversarioCenoura()

     def criarBoloMandioca(self):
        return AniversarioMandioca()


class FabricaInformal(FabricaBolo):

    def criarBoloChocolate(self):
        return InformalChocolate()

    def criarBoloCenoura(self):
        return InformalCenoura()

    def criarBoloMandioca(self):
        return InformalMandioca()


class FabricaCasamento(FabricaBolo):

    def criarBoloChocolate(self):
        return CasamentoChocolate()

    def criarBoloCenoura(self):
        return CasamentoCenoura()

    def criarBoloMandioca(self):
        return CasamentoMandioca()