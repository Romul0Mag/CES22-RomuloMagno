from Builder import *


class Diretor():
    def __init__(self):
        pass

    def fazerBoloChocolate(self, builder):
        builder.reset()
        builder.setSabor("Chocolate")


    def fazerBoloMandioca(self, builder):
        builder.reset()
        builder.setSabor("Mandioca")

    def fazerBoloCenoura(self, builder):
        builder.reset()
        builder.setSabor("Cenoura")

