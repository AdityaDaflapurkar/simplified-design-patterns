from abc import ABC, abstractmethod

class Component1:
    """
    First type of Product
    """
    def __init__(self, prop1, prop2, prop3):
        self.prop1 = prop1
        self.prop2 = prop2
        self.prop3 = prop3
        
    def desc(self):
        return 'Component1(prop1={}, prop2={}, prop3={})'.format(self.prop1, self.prop2, self.prop3)

class Component2:
    """
    Second type of Product
    """
    def __init__(self, prop1):
        self.prop1 = prop1

    def desc(self):
        return 'Component2(prop1={})'.format(self.prop1)

class Component3:
    """
    Third type of Product
    """
    def __init__(self, prop1, prop2):
        self.prop1 = prop1
        self.prop2 = prop2

    def desc(self):
        return 'Component3(prop1={}, prop2={})'.format(self.prop1, self.prop2)

class Product:
    """
    Represent the complex object under construction.
    """
    def __init__(self):
        self.component1 = None
        self.component2 = None
        self.component3 = None

    def display(self):
        print('Class:Product(')
        print('component1:{}'.format(self.component1.desc()))
        print('component2:{}'.format(self.component2.desc()))
        print('component3:{}'.format(self.component3.desc()))
        print(')')

class Client:
    """
    Construct an object using the Builder interface.
    """
    def __init__(self):
        self.product = None


    def build_product(self, builder):
        builder.build_component1(1, 2, 3)
        builder.build_component2(4)
        builder.build_component3(5, 6)
        self.product = builder.build()

    def display_product(self):
        self.product.display()

class Builder(ABC):
    """
    Specify an abstract interface for creating parts of a Product
    object.
    """

    def __init__(self):
        self.product = Product()

    @abstractmethod
    def build_component1(self):
        pass

    @abstractmethod
    def build_component2(self):
        pass

    @abstractmethod
    def build_component3(self):
        pass

    def build(self):
        return self.product

class ConcreteBuilder(Builder):
    """
    Construct and assemble parts of the product by implementing the
    Builder interface.
    Define and keep track of the representation it creates.
    Provide an interface for retrieving the product.
    """

    def build_component1(self, prop1, prop2, prop3):
        self.product.component1 = Component1(prop1, prop2, prop3)

    def build_component2(self, prop1):
        self.product.component2 = Component2(prop1)

    def build_component3(self, prop1, prop2):
        self.product.component3 = Component3(prop1, prop2)

def main():
    concrete_builder = ConcreteBuilder()
    client = Client()
    client.build_product(concrete_builder)
    client.display_product()


if __name__ == "__main__":
    main()
