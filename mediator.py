from abc import ABC, abstractmethod
class BaseComponent:
    def __init__(self):
        self._mediator = None
    
    def set_mediator(self, mediator):
        self._mediator = mediator

class Component1(BaseComponent):
    def method1(self):
        print('Component1()::method1()')
        self._mediator.notify_method(1)

    def method2(self):
        print('Component1()::method2()')
        self._mediator.notify_method(2)

class Component2(BaseComponent):
    def method3(self):
        print('Component2()::method3()')
        self._mediator.notify_method(3)

    def method4(self):
        print('Component2()::method4()')
        self._mediator.notify_method(4)

class Mediator(ABC):
    def notify(self, sender: object, event: str) -> None:
        pass

class ConcreteMediator:
    def __init__(self, component1: Component1, component2: Component2):
        self._component1 = component1
        self._component2 = component2
        self._component1.set_mediator(self)
        self._component2.set_mediator(self)

    def notify_method(self, event):
        if event == 1:
            self._component2.method3()
        elif event == 2:
            print('Mediator::notify(2)')
        elif event == 3:
            self._component1.method2()
            self._component2.method4()
        elif event == 4:
            print('Mediator::notify(4)')

class Client:
    def run_mediator(self):
        c1 = Component1()
        c2 = Component2()
        ConcreteMediator(c1, c2)

        c1.method1()

if __name__ == "__main__":
    client = Client()
    client.run_mediator()
        

