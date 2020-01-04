from abc import ABC, abstractmethod


class Context(ABC):
    _state = None
    
    def __init__(self, state):
        self.transition_to(state)

    def transition_to(self, state):
        self._state = state
        self._state.context = self

    def request1(self):
        self._state.handle1()

    def request2(self):
        self._state.handle2()


class State(ABC):
    context = None

    @abstractmethod
    def handle1(self) -> None:
        pass

    @abstractmethod
    def handle2(self) -> None:
        pass

class ConcreteState1(State):
    def handle1(self) -> None:
        print("ConcreteState1 handles request1.")
        print("ConcreteState1 wants to change the state of the context.")
        self.context.transition_to(ConcreteState2())

    def handle2(self) -> None:
        print("ConcreteState1 handles request2.")


class ConcreteState2(State):
    def handle1(self) -> None:
        print("ConcreteState2 handles request1.")

    def handle2(self) -> None:
        print("ConcreteState2 handles request2.")
        print("ConcreteState2 wants to change the state of the context.")
        self.context.transition_to(ConcreteState1())


class Client:
    def run_state(self):
        context = Context(ConcreteState1())
        context.request1()
        context.request2()

if __name__ == "__main__":
    client = Client()
    client.run_state()