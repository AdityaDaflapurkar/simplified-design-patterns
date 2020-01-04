from abc import ABC, abstractmethod

class Component(ABC):
    @abstractmethod
    def accept(self, visitor):
        pass

class ConcreteComponent1(Component):
    def accept(self, visitor):
        visitor.visit_concrete_component_1(self)

    def method1(self):
        print('ConcreteComponent1::method1()')

class ConcreteComponent2(Component):
    def accept(self, visitor):
        visitor.visit_concrete_component_2(self)
    
    def method1(self):
        print('ConcreteComponent2::method1()')

    def method2(self):
        print('ConcreteComponent2::method2()')

class Visitor(ABC):
    @abstractmethod
    def visit_concrete_component_1(self, component: ConcreteComponent1):
        pass

    @abstractmethod
    def visit_concrete_component_2(self, component: ConcreteComponent2):
        pass

class ConcreteVisitor1(Visitor):
    def visit_concrete_component_1(self, component):
        print('ConcreteVisitor1::visit_concrete_component_1()')

    def visit_concrete_component_2(self, component) -> None:
        print('ConcreteVisitor1::visit_concrete_component_2()')
        component.method1()


class ConcreteVisitor2(Visitor):
    def visit_concrete_component_1(self, component):
        print('ConcreteVisitor2::visit_concrete_component_1()')
        component.method1()
        

    def visit_concrete_component_2(self, component):
        component.method2()
        component.method1()
        print('ConcreteVisitor2::visit_concrete_component_2()')


class Client:
    def run_visitor(self, visitor):
        components = [ConcreteComponent1(), ConcreteComponent2()]
        for component in components:
            component.accept(visitor)

if __name__ == "__main__":
    client = Client()
    client.run_visitor(ConcreteVisitor1())
    client.run_visitor(ConcreteVisitor2())