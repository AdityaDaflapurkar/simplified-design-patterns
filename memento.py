from abc import ABC, abstractmethod
import random 
class Memento(ABC):

    @abstractmethod
    def get_state(self) -> str:
        pass


class ConcreteMemento(Memento):
    def __init__(self, state):
        self._state = state

    def get_state(self):
        return self._state

class Originator():
    def __init__(self, state):
        self._state = state

    def do_something(self) -> None:
        self._state = random.uniform(5,10) 


    def save(self) -> Memento:
        return ConcreteMemento(self._state)

    def restore(self, memento: Memento) -> None:
        self._state = memento.get_state()

class Caretaker():
    def __init__(self, originator: Originator) -> None:
        self._mementos = []
        self._originator = originator

    def backup(self) -> None:
        self._mementos.append(self._originator.save())

    def undo(self) -> None:
        if not len(self._mementos):
            return

        memento = self._mementos.pop()
        try:
            self._originator.restore(memento)
        except Exception:
            self.undo()

    def show_history(self) -> None:
        for memento in self._mementos:
            print(memento.get_state())


if __name__ == "__main__":
    originator = Originator("Super-duper-super-puper-super.")
    caretaker = Caretaker(originator)

    caretaker.backup()
    originator.do_something()

    caretaker.backup()
    originator.do_something()

    caretaker.backup()
    originator.do_something()

    print()
    caretaker.show_history()

    print("\nClient: Now, let's rollback!\n")
    caretaker.undo()

    print("\nClient: Once more!\n")
    caretaker.undo()
