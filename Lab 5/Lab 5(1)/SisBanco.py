from Cliente import Cliente
from tkinter import *
import Command


class SisBanco:
    def __init__(self, cliente, master = None):
        self.comandos = []
        self.cliente = cliente
        self.fonte = ("Verdana", "8")

        self.container1 = Frame(master)
        self.container1["pady"] = 10
        self.container1.pack()
        self.container2 = Frame(master)
        self.container2["padx"] = 20
        self.container2["pady"] = 5
        self.container2.pack()
        self.container3 = Frame(master)
        self.container3["padx"] = 20
        self.container3["pady"] = 5
        self.container3.pack()
        self.container4 = Frame(master)
        self.container4["padx"] = 20
        self.container4["pady"] = 5
        self.container4.pack()
        self.container5 = Frame(master)
        self.container5["padx"] = 20
        self.container5["pady"] = 5
        self.container5.pack()
        self.container6 = Frame(master)
        self.container6["padx"] = 20
        self.container6["pady"] = 5
        self.container6.pack()
        self.container7 = Frame(master)
        self.container7["padx"] = 20
        self.container7["pady"] = 5
        self.container7.pack()
        self.container8 = Frame(master)
        self.container8["padx"] = 20
        self.container8["pady"] = 5
        self.container8.pack()
        self.container9 = Frame(master)
        self.container9["padx"] = 20
        self.container9["pady"] = 5
        self.container9.pack()
        self.container10 = Frame(master)
        self.container10["padx"] = 20
        self.container10["pady"] = 5
        self.container10.pack()
        self.container11 = Frame(master)
        self.container11["padx"] = 20
        self.container11["pady"] = 5
        self.container11.pack()

        self.titulo = Label(self.container1, text=f'{self.cliente.nome}')
        self.titulo["font"]= ("Calibri", "9", "bold")
        self.titulo.pack()

        self.btnVerificarSaldo = Button(self.container2, text="Verificar Saldo", font=self.fonte, width=15)
        self.btnVerificarSaldo["command"]=self.VerificarSaldo
        self.btnVerificarSaldo.pack(side=LEFT)


        self.lblsaldo = Label(self.container2, text="Saldo:", font=self.fonte, width = 15)
        self.lblsaldo.pack(side=LEFT)

        self.txtsaldo= Entry(self.container2)
        self.txtsaldo["width"] = 10
        self.txtsaldo["font"] = self.fonte
        self.txtsaldo.pack(side=RIGHT)

        self.btnTransferir = Button(self.container3, text="Transferir", font=self.fonte, width=15)
        self.btnTransferir["command"]=self.Transferir
        self.btnTransferir.pack(side=LEFT)

        self.lbltransferencia = Label(self.container3, text="Valor:", font=self.fonte, width = 15)
        self.lbltransferencia.pack(side=LEFT)

        self.txttransferencia= Entry(self.container3)
        self.txttransferencia["width"] = 10
        self.txttransferencia["font"] = self.fonte
        self.txttransferencia.pack(side=RIGHT)

        self.btnReceber = Button(self.container4, text="Receber", font=self.fonte, width=15)
        self.btnReceber["command"]=self.Receber
        self.btnReceber.pack(side=LEFT)

        self.lblreceber = Label(self.container4, text="Valor:", font=self.fonte, width = 15)
        self.lblreceber.pack(side=LEFT)

        self.txtreceber= Entry(self.container4)
        self.txtreceber["width"] = 10
        self.txtreceber["font"] = self.fonte
        self.txtreceber.pack(side=RIGHT)

        self.btnExtrato = Button(self.container5, text="Extrato", font=self.fonte, width=15)
        self.btnExtrato["command"]=self.MostrarExtrato
        self.btnExtrato.pack(side = LEFT)

        self.lblextrato1 = Label(self.container6, font=self.fonte, width = 15)
        self.lblextrato1.pack()

        self.lblextrato2 = Label(self.container7, font=self.fonte, width = 15)
        self.lblextrato2.pack()

        # self.btnHistorico = Button(self.container5, text="Atualizar Historico", font=self.fonte, width=15)
        # self.btnHistorico["command"]=self.MostrarHistorico
        # self.btnHistorico.pack(side = RIGHT)

        self.lblhistorico1 = Label(self.container8, font=self.fonte, width = 15)
        self.lblhistorico1.pack()

        self.lblhistorico2 = Label(self.container9, font=self.fonte, width = 15)
        self.lblhistorico2.pack()

        self.lblhistorico3 = Label(self.container10, font=self.fonte, width = 15)
        self.lblhistorico3.pack()

        self.lblhistorico4 = Label(self.container11, font=self.fonte, width = 15)
        self.lblhistorico4.pack()

    def VerificarSaldo(self):
        verifica = Command.VerificarSaldo(self.cliente)
        saldo_cliente = verifica.execute()
        self.txtsaldo.delete(0, END)
        self.txtsaldo.insert(INSERT, saldo_cliente)
        self.comandos.append("Verificou o saldo")
        self.MostrarHistorico()
        self.lblextrato1["text"] = ""
        self.lblextrato2["text"] = ""

    def Transferir(self):

        valor = self.txttransferencia.get()
        transfere = Command.Transferir(self.cliente, valor)
        transfere.execute()

        self.txttransferencia.delete(0, END)
        self.comandos.append(f'transferiu {valor} reais')
        self.MostrarHistorico()
        self.lblextrato1["text"] = ""
        self.lblextrato2["text"] = ""
        self.txtsaldo.delete(0, END)

    def Receber(self):

        valor = self.txtreceber.get()
        recebe = Command.Receber(self.cliente, valor)
        recebe.execute()


        self.txtreceber.delete(0, END)
        self.comandos.append(f'recebeu {valor} reais')
        self.MostrarHistorico()
        self.lblextrato1["text"] = ""
        self.lblextrato2["text"] = ""
        self.txtsaldo.delete(0, END)

    def MostrarExtrato(self):
        self.lblextrato1["text"] = "Extrato:"
        self.lblextrato2["text"] = ""
        for i in range(3,0,-1):
            if len(self.cliente.extrato)-i >= 0:
                self.lblextrato2["text"] = self.lblextrato2["text"] + self.cliente.extrato[len(self.cliente.extrato)-i]
        self.comandos.append(f'Verificou o extrato')
        self.MostrarHistorico()

    def MostrarHistorico(self):
        self.lblhistorico1["text"] = "Historico:"

        if len(self.comandos)-3 >= 0:
            self.lblhistorico4["text"] =self.comandos[len(self.comandos)-3]

        if len(self.comandos)-2 >= 0:
            self.lblhistorico3["text"] =self.comandos[len(self.comandos)-2]

        if len(self.comandos)-1 >= 0:
            self.lblhistorico2["text"] =self.comandos[len(self.comandos)-1]


romulo = Cliente(0,"Romulo")
root = Tk()
SisBanco(romulo,root)
root.mainloop()


