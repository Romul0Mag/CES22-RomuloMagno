


class Compra():
    def __init__(self, i, ordem):
        self.index = i
        self.ordem = ordem

    def exporInfo(self):
        print(f'Compra {self.index}')
        for produto, quantidade in self.ordem.items():
            print(f'produto:{produto.titulo}, quantidade:{quantidade}')

