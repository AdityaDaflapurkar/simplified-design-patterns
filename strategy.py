from abc import ABC, abstractmethod

class Strategy(ABC):
    def execute(self):
        pass

class ConcreteStrategy1(Strategy):
    def execute(self):
        print('Executing strategy 1')


class ConcreteStrategy2(Strategy):
    def execute(self):
        print('Executing strategy 2')

class Context:
    def __init__(self, strategy: Strategy):
        self._strategy = strategy

    def method(self):
        self._strategy.execute()

class Client:
    def run_strategy(self, context):
        context.method()
    
if __name__ == "__main__":
    client = Client()
    ctx1 = Context(ConcreteStrategy1())
    client.run_strategy(ctx1)
    ctx2 = Context(ConcreteStrategy2())
    client.run_strategy(ctx2)