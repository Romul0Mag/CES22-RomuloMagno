from FabricaBolo import *

fabrica = FabricaAniversario()
fabrica.criarBoloChocolate().exporInfo()
fabrica.criarBoloMandioca().exporInfo()
fabrica.criarBoloCenoura().exporInfo()

print('\n')

fabrica = FabricaInformal()
fabrica.criarBoloChocolate().exporInfo()
fabrica.criarBoloMandioca().exporInfo()
fabrica.criarBoloCenoura().exporInfo()

print('\n')

fabrica = FabricaCasamento()
fabrica.criarBoloChocolate().exporInfo()
fabrica.criarBoloMandioca().exporInfo()
fabrica.criarBoloCenoura().exporInfo()
