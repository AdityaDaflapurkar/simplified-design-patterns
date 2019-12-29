from abc import ABC, abstractmethod
class CompatibleInterface(ABC):
    """
    The Target defines the domain-specific interface used by the client code.
    """
    @abstractmethod
    def compatible_interface_method1(self):
        pass

    @abstractmethod
    def compatible_interface_method2(self):
        pass

    @abstractmethod
    def compatible_interface_method3(self):
        pass


class CompatibleComponent1(CompatibleInterface):
    """
    The Target defines the domain-specific interface used by the client code.
    """

    def compatible_interface_method1(self):
        print('CompatibleComponent1()::compatible_interface_method1()')

    def compatible_interface_method2(self):
        print('CompatibleComponent1()::compatible_interface_method2()')

    def compatible_interface_method3(self):
        print('CompatibleComponent1()::compatible_interface_method3()')


class IncompatibleInterface(ABC):
    """
    The Target defines the domain-specific interface used by the client code.
    """
    @abstractmethod
    def incompatible_interface_method1(self):
        pass

    @abstractmethod
    def incompatible_interface_method2(self):
        pass

class IncompatibleComponent1(IncompatibleInterface):
    """
    The Adaptee contains some useful behavior, but its interface is incompatible
    with the existing client code. The Adaptee needs some adaptation before the
    client code can use it.
    """

    def incompatible_interface_method1(self):
        print('IncompatibleComponent1()::incompatible_interface_method1()')

    def incompatible_interface_method2(self):
        print('IncompatibleComponent1()::incompatible_interface_method2()')


class Adapter(CompatibleInterface):
    """
    The Adapter makes the Adaptee's interface compatible with the Target's
    interface.
    """

    def __init__(self, incompatible_component):
        self.incompatible_component = incompatible_component

    def compatible_interface_method1(self):
        self.incompatible_component.incompatible_interface_method1()

    def compatible_interface_method2(self):
        self.incompatible_component.incompatible_interface_method2()

    def compatible_interface_method3(self):
        print('CompatibleComponent1()::compatible_interface_method3()')

class Client():
    """
    The Adapter makes the Adaptee's interface compatible with the Target's
    interface.
    """

    def __init__(self, compatible_component: CompatibleInterface):
        self.compatible_component = compatible_component

    def call_method1(self):
        self.compatible_component.compatible_interface_method1()

    def call_method2(self):
        self.compatible_component.compatible_interface_method2()

    def call_method3(self):
        self.compatible_component.compatible_interface_method3()

    def run_adapter(self):
        self.call_method1()
        self.call_method2()
        self.call_method3()


if __name__ == "__main__":
    print('With compatible interface:')
    compatible_component = CompatibleComponent1()
    client1 = Client(compatible_component)
    client1.run_adapter()
    print('With adapted incompatible interface:')
    adapter = Adapter(IncompatibleComponent1())
    client2 = Client(adapter)
    client2.run_adapter()
    
