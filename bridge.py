from abc import ABC, abstractmethod

class Implementation(ABC):

    @abstractmethod
    def implementation_method1(self):
        pass

class ConcreteImplementation1(Implementation):
    def implementation_method1(self):
        print('ConcreteImplementation1::implementation_method1()')


class ConcreteImplementation2(Implementation):
    def implementation_method1(self):
        print('ConcreteImplementation2::implementation_method1')

        
class Abstraction(ABC):

    def __init__(self, implementation: Implementation):
        self.implementation = implementation

    @abstractmethod
    def abstraction_method1(self):
        pass

class ExtendedAbstraction(Abstraction):
    """
    You can extend the Abstraction without changing the Implementation classes.
    """

    def abstraction_method1(self):
        print('ExtendedAbstraction::abstraction_method1()')

    def run_all(self):
        self.abstraction_method1()
        self.implementation.implementation_method1()


class Client():
    """
    The Adapter makes the Adaptee's interface compatible with the Target's
    interface.
    """
    def run_bridge(self, abstraction):
        abstraction.run_all()

if __name__ == "__main__":
    """
    The client code should be able to work with any pre-configured abstraction-
    implementation combination.
    """

    implementation = ConcreteImplementation1()
    abstraction1 = ExtendedAbstraction(implementation)
    client = Client()
    client.run_bridge(abstraction1)

    implementation = ConcreteImplementation2()
    abstraction2 = ExtendedAbstraction(implementation)
    client = Client()
    client.run_bridge(abstraction2)
