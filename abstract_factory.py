from abc import ABC, abstractmethod
class ProductA(ABC):
    @abstractmethod
    def product_a_method1(self):
        pass


class ConcreteProductA1(ProductA):
    def product_a_method1(self):
        print('ConcreteProductA1()::product_method1()')


class ConcreteProductA2(ProductA):
    def product_a_method1(self):
        print('ConcreteProductA2()::product_method1()')


class ProductB(ABC):
    @abstractmethod
    def product_b_method1(self):
        pass


class ConcreteProductB1(ProductB):
    def product_b_method1(self):
        print('ConcreteProductB1()::product_method1()')


class ProductC(ABC):
    @abstractmethod
    def product_c_method1(self):
        pass

class ConcreteProductC1(ProductC):
    def product_c_method1(self):
        print('ConcreteProductC1()::product_method1()')


class ConcreteProductC2(ProductC):
    def product_c_method1(self):
        print('ConcreteProductC2()::product_method1()')

class ConcreteProductC3(ProductC):
    def product_c_method1(self):
        print('ConcreteProductC3()::product_method1()')

class AbstractFactory(ABC):
    @abstractmethod
    def create_product_a(self):
        pass

    @abstractmethod
    def create_product_b(self):
        pass

    @abstractmethod
    def create_product_c(self):
        pass


class ConcreteFactory1(AbstractFactory):
    def create_product_a(self):
        return ConcreteProductA1()

    def create_product_b(self):
        return ConcreteProductB1()
    
    def create_product_c(self):
        return ConcreteProductC3()


class ConcreteFactory2(AbstractFactory):
    def create_product_a(self):
        return ConcreteProductA2()

    def create_product_b(self):
        return ConcreteProductB1()

    def create_product_c(self):
        return ConcreteProductC2()

class Client:
    def run_abstract_factory(self, factory):
        resA, resB, resC = factory.create_product_a(), factory.create_product_b(), factory.create_product_c()
        resA.product_a_method1()
        resB.product_b_method1()
        resC.product_c_method1()

if __name__ == "__main__":
    client1 = Client()
    client1.run_abstract_factory(ConcreteFactory1())

    client2 = Client()
    client2.run_abstract_factory(ConcreteFactory2())



