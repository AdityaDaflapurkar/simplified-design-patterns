from abc import ABC, abstractmethod


class Receiver:
    def method1(self, prop1):
        print('Receiver(prop1={})::method1()'.format(prop1))

    def method2(self, prop1, prop2):
        print('Receiver(prop1={}, prop2={})::method2()'.format(prop1, prop2))

    def method3(self, prop1):
        print('Receiver(prop1={})::method3()'.format(prop1))

    def method4(self):
        print('Receiver()::method4()')

class Command(ABC):
    @abstractmethod
    def execute(self):
        pass

class ConcreteCommand1(Command):
    def __init__(self, receiver: Receiver, prop1, prop2):
        self._receiver = receiver
        self._prop1 = prop1
        self._prop2 = prop2

    def execute(self):
        self._receiver.method2(self._prop1, self._prop2)
        self._receiver.method4()
        

class ConcreteCommand2(Command):
    def __init__(self, prop1, prop2, prop3):
        self._prop1 = prop1
        self._prop2 = prop2
        self._prop3 = prop3

    def execute(self):
        print('ConcreteCommand2(prop1={}, prop2={}, prop3={})::execute()'.format(self._prop1, self._prop2, self._prop3))

    
class Invoker:
    def __init__(self, command):
        self._action_on_event1 = command
    def on_event1(self):
        self._action_on_event1.execute()

class Client: 
    def run_command(self):
        command1 = ConcreteCommand1(Receiver(), 1, 2)
        command2 = ConcreteCommand2(1, 1, 3)
        invoker = Invoker(command1)
        invoker.on_event1()
        invoker = Invoker(command2)
        invoker.on_event1()

if __name__ == "__main__":
    client = Client()
    client.run_command()