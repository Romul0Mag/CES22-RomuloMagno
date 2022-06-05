from Compra import Compra


class Pessoa():
    def __init__(self, nome):
        self.nome = nome
        self.email = ""


class Cliente(Pessoa):
    def __init__(self, nome):
        super().__init__(nome)
        self.compras = []
        self.cont = 1

    def exporInfo(self):
        print(f'nome: {self.nome} \n'
              f'email: {self.email}')
        for compra in self.compras:
            compra.exporInfo()

    def inserirOrdem(self, ordem):
        self.compras.append(Compra(self.cont, ordem))
        self.cont += 1

    def buscarOrdem(self, i):
        for compra in self.compras:
            if compra.index > i:
                print('não existe essa ordem de compra')
                return None
            if compra.index == i:
                return compra

    def consultarOrdem(self, i):
        a = self.buscarOrdem(i)
        if(a is not None):
            a.exporInfo()
        else:
            print(f'não existe a ordem de compra {i}')

    def alterarOrdem(self, ordem, i):
        a = self.buscarOrdem(i)
        if (a):
            a.ordem = ordem
        else:
            print(f'não existe a ordem de compra {i}')


    def removerOrdem(self, i):
        a = self.buscarOrdem(i)
        if (a):
            self.compras.remove(a)
            print(f'ordem de compra {i} removida')
        else:
            print(f'não existe a ordem de compra {i}')

class Autor(Pessoa):
    def __init__(self, nome):
        super().__init__(nome)
        self.livros = []

    def exporLivros(self):
        for livro in self.livros:
            livro.exporProduto()