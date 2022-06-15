# Decorator/alldecorators/CoffeeShop.py
# Coffee example using decorators
class PizzaComponent:
    def getDescription(self):
        return self.__class__.__name__

    def getTotalCost(self):
        return self.__class__.cost


class Dough(PizzaComponent):
    cost = 30.0

class Decorator(PizzaComponent):
    def __init__(self, pizzaComponent):
        self.component = pizzaComponent

    def getTotalCost(self):
        return self.component.getTotalCost() + PizzaComponent.getTotalCost(self)

    def getDescription(self):
        return self.component.getDescription() + ' '+ PizzaComponent.getDescription(self)


class Mozzarella(Decorator):
    cost = 5.0
    def __init__(self, drinkComponent):
        Decorator.__init__(self, drinkComponent)


class Chocolate(Decorator):
    cost = 15.0
    def __init__(self, drinkComponent):
        Decorator.__init__(self, drinkComponent)


class Pepperoni(Decorator):
    cost = 5.5
    def __init__(self, drinkComponent):
        Decorator.__init__(self, drinkComponent)


class Onion(Decorator):
    cost = 2.5
    def __init__(self, drinkComponent):
        Decorator.__init__(self, drinkComponent)

