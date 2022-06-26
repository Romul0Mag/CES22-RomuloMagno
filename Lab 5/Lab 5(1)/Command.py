from Cliente import Cliente


class Command():
    def __init__(self):
        pass

    def execute(self):
        pass

class VerificarSaldo(Command):
    def __init__(self, cliente):
        super().__init__()
        self.cliente = cliente

    def execute(self):
        return self.cliente.saldo

class Transferir(Command):
    def __init__(self, cliente, valor):
        super().__init__()
        self.cliente = cliente
        self.valor = valor

    def execute(self):
        self.cliente.saldo =  self.cliente.saldo - float(self.valor)
        self.cliente.extrato.append(f'-{self.valor}')


class Receber(Command):
    def __init__(self, cliente, valor):
        super().__init__()
        self.cliente = cliente
        self.valor = valor

    def execute(self):
        self.cliente.saldo = self.cliente.saldo + float(self.valor)
        self.cliente.extrato.append(f'+{self.valor}')