from abc import ABC, abstractmethod
class Component(ABC):
    @abstractmethod
    def method1(self):
        pass

class ConcreteComponent(Component):
    def method1(self):
        print('ConcreteComponent1()::method1()')

class Decorator(Component):
    def __init__(self, component: Component):
        self._component = component

    @abstractmethod
    def method2(self):
        pass

class ConcreteDecorator1(Decorator):
    def method1(self):
        self.method2()
        self._component.method1()
        self.method3()
    
    def method2(self):
        print('ConcreteDecorator1()::method2()')

    def method3(self):
        print('ConcreteDecorator1()::method3()')


class ConcreteDecorator2(Decorator):
    def method1(self):
        self.method2()
        self._component.method1()
        self.method4()
        self.method5()
    
    def method2(self):
        print('ConcreteDecorator2()::method2()')
    
    def method4(self):
        print('ConcreteDecorator2()::method4()')

    def method5(self):
        print('ConcreteDecorator2()::method5()')

class Client:
    def run_decorator(self, component:Component):
        component.method1()

if __name__ == "__main__":
    simple_component = ConcreteComponent()
    decorated_component1 = ConcreteDecorator1(simple_component)
    decorated_component2 = ConcreteDecorator2(simple_component)
    chain_decorated_component =  ConcreteDecorator2(ConcreteDecorator1(simple_component))
    
    client = Client()
    print('Running simple component:')
    client.run_decorator(simple_component)
    print('Running decorator1 component:')
    client.run_decorator(decorated_component1)
    print('Running decorator2 component:')
    client.run_decorator(decorated_component2)
    print('Running chain decorated component:')
    client.run_decorator(chain_decorated_component)

