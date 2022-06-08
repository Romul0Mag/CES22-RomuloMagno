from Diretor import *


diretor = Diretor()
builder = AniversarioBuilder()
diretor.fazerBoloChocolate(builder)
builder.getResult().exporInfo()
diretor.fazerBoloMandioca(builder)
builder.getResult().exporInfo()
diretor.fazerBoloCenoura(builder)
builder.getResult().exporInfo()

print('\n')

builder = InformalBuilder()
diretor.fazerBoloChocolate(builder)
builder.getResult().exporInfo()
diretor.fazerBoloMandioca(builder)
builder.getResult().exporInfo()
diretor.fazerBoloCenoura(builder)
builder.getResult().exporInfo()

print('\n')

builder = CasamentoBuilder()
diretor.fazerBoloChocolate(builder)
builder.getResult().exporInfo()
diretor.fazerBoloMandioca(builder)
builder.getResult().exporInfo()
diretor.fazerBoloCenoura(builder)
builder.getResult().exporInfo()