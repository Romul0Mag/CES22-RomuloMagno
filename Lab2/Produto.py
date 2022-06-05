import abc
from Pessoa import *


class Produto():
    __metaclass__ = abc.ABCMeta
    def __init__(self, titulo, venda, compra, imposto,calculadora_imposto):
        self.titulo = titulo
        self.preco_venda = venda
        self.preco_compra = compra
        self.calculadora_imposto = calculadora_imposto
        self.imposto = imposto


    def setImposto(self):
        self.imposto = self.calculadora_imposto.calcularImposto(self)

    @abc.abstractmethod
    def alterarProduto(self, **kw):
        pass

    @abc.abstractmethod
    def removerProduto(self, Livraria):
        pass

    @abc.abstractmethod
    def inserirProduto(self, Livraria):
        pass

    @abc.abstractmethod
    def exporProduto(self):
        pass

class Livro(Produto):
    def __init__(self, titulo, venda, compra, imposto, calculadora_imposto, autor, genero, edicao, editora):
        super().__init__( titulo, venda, compra, imposto, calculadora_imposto)
        self.autor = autor
        self.genero = genero
        self.edicao = edicao
        self.editora = editora

    def alterarProduto(self, **kw):
        for key, value in kw.items():
            if hasattr(self, key):
                setattr(self, key, value)

    def removerProduto(self, Livraria):
        for autor in Livraria.autores:
            for livro in autor.livros:
                if livro == self:
                    autor.livros.remove(self)

    def inserirProduto(self, Livraria):
        achou = 0
        for autor in Livraria.autores:
            if autor.nome == self.autor.nome:
                autor.livros.append(self)
                achou = 1

        if not achou :
            a = Autor(self.autor.nome)
            Livraria.autores.append(a)
            a.livros.append(self)


    def exporProduto(self):
        print(f'\n preço de venda: {self.preco_venda}\n'
              f'preço de compra: {self.preco_compra}\n'
              f'valor do imposto: {self.imposto}\n'
              f'titulo: {self.titulo}\n'
              f'autor: {self.autor.nome}\n'
              f'edicao: {self.edicao}\n'
              f'editora: {self.editora}\n'
              f'genero:{self.genero.nome}\n')

