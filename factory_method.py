"""
Factory method pattern defines an interface for creating an object, but lets subclasses decide
which class to instantiate.
"""
from abc import ABC, abstractmethod

class Product(ABC):
    """
    Interface for Product object created by factory method
    """
    @abstractmethod
    def product_method1(self):
        pass

class ConcreteProduct1(Product):
    """
    First type of Product
    """
    def __init__(self, prop1, prop2, prop3):
        self.prop1 = prop1
        self.prop2 = prop2
        self.prop3 = prop3
        
    def product_method1(self):
        print('ConcreteProduct1(prop1={}, prop2={}, prop3={})::product_method1()'.format(self.prop1, self.prop2, self.prop3))

class ConcreteProduct2(Product):
    """
    Second type of Product
    """
    def __init__(self, prop1):
        self.prop1 = prop1

    def product_method1(self):
        print('ConcreteProduct2(prop1={})::product_method1()'.format(self.prop1))

class Creator(ABC):
    """
    Creator interface for creating Product object 
    """
    @abstractmethod
    def _factory_method(self):
        pass

class ConcreteCreator1(Creator):
    """
    Implementation of Creator interface which returns ConcreteProduct1 object
    """

    def _factory_method(self):
        return ConcreteProduct1(1, 2, 3)

class ConcreteCreator2(Creator):
    """
    Implementation of Creator interface which returns ConcreteProduct2 object
    """
    def _factory_method(self):
        return ConcreteProduct2(1)

class Client:
    def run_factory_method(self, creator):
        res = creator._factory_method()
        res.product_method1()

if __name__ == "__main__":
    client1 = Client()
    client1.run_factory_method(ConcreteCreator1())

    client2 = Client()
    client2.run_factory_method(ConcreteCreator2())