from Compra import *
from Pessoa import *
from Livraria import *
from Genero import *
from Produto import *
from CalculadoraImposto import *

saraiva = Livraria("Saraiva")
calc = ImpostoLivroBR2022()
JK = Autor("JK")
HP = Livro("Harry Potter",50, 30, 0, calc,  JK, aventura_fantasia, 3, "editoraJK" )
HP.setImposto()

saraiva.inserirCliente("Romulo")
saraiva.consultarCliente("Romulo")
saraiva.alterarCliente("Romulo", "abc@gmail.com")
Romulo = saraiva.consultarCliente("Romulo")

print("\n")

saraiva.inserirProduto(HP, 100)
saraiva.consultarProduto(HP)
saraiva.alterarProduto(HP, preco_venda=55)
saraiva.consultarProduto(HP)

saraiva.consultarAutor("JK")

saraiva.inserirOrdemCompra({HP :3}, Romulo)
saraiva.consultarOrdemCompra(1,Romulo)
saraiva.inserirOrdemCompra({HP :5}, Romulo)
saraiva.consultarOrdemCompra(2,Romulo)
saraiva.alterarOrdemCompra({HP :4}, 1, Romulo)
saraiva.consultarOrdemCompra(1,Romulo)
saraiva.removerOrdemCompra(2,Romulo)
saraiva.consultarOrdemCompra(2,Romulo)

print("\n")

saraiva.removerProduto(HP)
saraiva.consultarProduto(HP)

print("\n")

saraiva.removerCliente("Romulo")
saraiva.consultarCliente("Romulo")

