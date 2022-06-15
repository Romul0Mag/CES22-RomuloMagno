from PizzaShop import *


pepperoni = Pepperoni(Onion(Mozzarella(Dough())))
print(pepperoni.getDescription()+ ": $" + str(pepperoni.getTotalCost()))
chocolate = Chocolate(Mozzarella(Dough()))
print(chocolate.getDescription()+ ": $" + str(chocolate.getTotalCost()))
