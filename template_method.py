from abc import ABC, abstractmethod

class Component(ABC):
    """
    Interface for Component object created by factory method
    """
    def template_method(self):
        self.oper1()
        self.method1()
        self.oper2()

    def oper1(self):
        print('Component::oper1()')

    def oper2(self):
        print('Component::oper2()')

    @abstractmethod
    def method1(self):
        pass

class ConcreteComponent1(Component):
    def method1(self):
        print('ConcreteComponent1::method1()')

class ConcreteComponent2(Component):
    def method1(self):
        print('ConcreteComponent2::method1()')

class Client:
    def run_template_method(self, component):
        print('Running template method')
        component.template_method()
        print()

if __name__ == "__main__":
    client1 = Client()
    client1.run_template_method(ConcreteComponent1())

    client2 = Client()
    client2.run_template_method(ConcreteComponent2())