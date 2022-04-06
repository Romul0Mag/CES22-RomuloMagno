import abc

class Store():
    __metaclass__ = abc.ABCMeta

    #usei um método abstrato, pois todos que herdam de loja devem ter uma função própria para mostrar seu inventório
    @abc.abstractmethod
    def inventory(self):
        '''approach client'''

class CellphoneStore(Store):
    employees = ["seller", "manager"]

    def __init__(self, name, brands):
        self.brands = brands
        self.name = name

    #não precisa de uma instância para ser utilizada
    @classmethod
    def list_employees(cls):
        for employee in cls.employees:
            print(employee)

    def inventory(self):
        print("We have:")
        for brand in self.brands:
            print(brand)

    #não utiliza/modifica atributos do objeto/classe
    @staticmethod
    def approach():
        print("Hello, come in to see our products")

    #acessa/modifica atributos do objeto/classe
    def add_name(self, addition):
        self.name = self.name + "" + addition


MyStore = CellphoneStore("Tech",["Apple", "Samsung"])
MyStore.list_employees()
print('\n')
MyStore.inventory()
print('\n')
MyStore.approach()
print('\n')
MyStore.add_name("nology")
print(MyStore.name)