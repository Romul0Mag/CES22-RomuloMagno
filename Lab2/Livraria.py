from Pessoa import Cliente, Autor


class Livraria():
    def __init__(self, nome):
        self.estoque = {}
        self.autores = []
        self.clientes = []
        self.nome = nome

    def inserirOrdemCompra(self, ordem, cliente):
        cliente.inserirOrdem(ordem)

    def removerOrdemCompra(self, index, cliente):
        cliente.removerOrdem(index)

    def alterarOrdemCompra(self, ordem, index, cliente):
        cliente.alterarOrdem(ordem, index)

    def consultarOrdemCompra(self, index, cliente):
        cliente.consultarOrdem(index)

    def inserirCliente(self, nome):
        novo_cliente = Cliente(nome)
        self.clientes.append(novo_cliente)

    def removerCliente(self, nome):
        for cliente in self.clientes:
            if cliente.nome == nome:
                self.clientes.remove(cliente)
                print(f" cliente {cliente.nome} removido ")
                break

    def alterarCliente(self, nome, email):
        for cliente in self.clientes:
            if cliente.nome == nome:
                cliente.email = email

    def consultarCliente(self, nome):
        achou = 0
        for cliente in self.clientes:
            if cliente.nome == nome:
                cliente.exporInfo()
                achou = 1
                return cliente
        if not achou:
            print("esse cliente não existe")

    def consultarAutor(self, nome):
        for autor in self.autores:
            if autor.nome == nome:
                print(f"\n o autor {autor.nome} tem os seguintes livros:")
                autor.exporLivros()

    def inserirProduto(self, produto, quantidade):
        achou = 0
        for prod, quant in self.estoque.items():
            if prod == produto:
                achou = 1
                self.estoque[prod] += quantidade
                produto.inserirProduto(self)

        if not achou:
            self.estoque[produto] = quantidade
            produto.inserirProduto(self)

    def removerProduto(self, produto):
        achou = 0
        for prod, quant in self.estoque.items():
            if prod == produto:
                achou = 1
                del self.estoque[prod]
                produto.removerProduto(self)
                break

        if not achou:
            print('esse produto não esta no estoque')

    def alterarProduto(self, produto, **kw):
        achou = 0
        for prod, quant in self.estoque.items():
            if prod == produto:
                achou = 1
                prod.alterarProduto(**kw)

        if not achou:
            print('esse produto não esta no estoque')

    def consultarProduto(self, produto):
        achou = 0
        for prod, quant in self.estoque.items():
            if prod == produto:
                achou = 1
                print(f'tem {quant} desse produto no estoque')
                produto.exporProduto()

        if not achou:
            print('esse produto não esta no estoque')

