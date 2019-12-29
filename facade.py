class Component1:
    def method1(self):
        print('Component1()::method1()')

    def method2(self):
        print('Component1()::method2()')

    def method3(self):
        print('Component1()::method3()')


class Component2:
    def method1(self):
        print('Component2()::method1()')

    def method2(self):
        print('Component2()::method2()')

    def method3(self):
        print('Component2()::method3()')

    def method4(self):
        print('Component2()::method4()')

    def method5(self):
        print('Component2()::method5()')

class Facade:
    def __init__(self, component1: Component1, component2: Component2):
        self.component1 = component1
        self.component2 = component2

    def simple_interface_method1(self):
        self.component1.method1()
        self.component1.method2()
        self.component2.method1()
        self.component2.method2()
        self.component2.method3()

    def simple_interface_method2(self):
        self.component1.method2()
        self.component1.method3()
        self.component2.method4()
        self.component2.method5()

class Client:
    def run_facade(self, facade: Facade):
        print('Running simple interface method 1:')
        facade.simple_interface_method1()
        print('Running simple interface method 2:')
        facade.simple_interface_method2()

if __name__ == "__main__":
    facade = Facade(Component1(), Component2())
    client = Client()
    client.run_facade(facade)