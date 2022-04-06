class Food:
    def __init__(self):
        print("I'm food")
        print("I have flavour")


class CocoaBased(Food):
    def __init__(self):
        print("I'm cocoa based")
        super().__init__()
        print("I have cocoa")


class StrawberryBased(Food):
    def __init__(self):
        print("I'm strawberry based")
        print("I have strawberry")


class Sweet(Food):
    def __init__(self):
        print("I´m sweet")
        super().__init__()
        print("I have sugar")


class Chocolate(CocoaBased,Sweet):
    def __init__(self):
        print("I'm chocolate")
        super().__init__()
        print("I have a lot of calories")

class StrawberryMousse(StrawberryBased, Sweet):
    def __init__(self):
        print("I'm Strawberry Mousse")
        super().__init__()
        print("I have chantilly")


class StrawberryGelatin(Sweet, StrawberryBased):
    def __init__(self):
        print("I'm Strawberry Gelatin")
        super().__init__()
        print("I have gelatin")

class StrawberryChocolatePizza(StrawberryBased, CocoaBased):
    def __init__(self):
        print("I'm Strawberry & Chocolate Pizza")
        super().__init__()
        print("I have pizza dough")

#as 2 classes pais tem super() no init, logo chama o init dos 2 pais e do avô
kit_kat = Chocolate()
print(kit_kat.__class__.mro())
print("\n\n")

#primeira classe pai nao tem super() no init, logo nem entra no init da segunda
swift = StrawberryMousse()
print(swift.__class__.mro())
print("\n\n")

#primeira classe pai tem super() no init, logo entra no init da segunda e
# como este não tem super() ele não chama o init da classe "avó"
dr_oekler = StrawberryGelatin()
print(dr_oekler.__class__.mro())
print("\n\n")

#ambos os pais não têm super() no init, logo, entra só na primeira
pizza = StrawberryChocolatePizza()
print(pizza.__class__.mro())


