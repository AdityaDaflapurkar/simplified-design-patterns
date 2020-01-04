import random
class Memento:
    def __init__(self, state):
        self._state = state

    def get_state(self):
        return self._state

class Originator:
    def __init__(self, state):
        self._state = state

    def update_state(self) -> None:
        self._state = random.uniform(1,10) 

    def save(self) -> Memento:
        return Memento(self._state)

    def restore(self, memento: Memento) -> None:
        self._state = memento.get_state()

class Caretaker:
    def __init__(self, originator: Originator) -> None:
        self._mementos = []
        self._originator = originator

    def backup(self) -> None:
        self._mementos.append(self._originator.save())

    def undo(self) -> None:
        print('Undo')
        print()
        if not len(self._mementos):
            return

        memento = self._mementos.pop()
        try:
            self._originator.restore(memento)
        except Exception:
            self.undo()

    def show_history(self) -> None:
        print('History')
        for memento in self._mementos:
            print(memento.get_state())
        print()

class Client:
    def run_memento(self):
        originator = Originator(1)
        caretaker = Caretaker(originator)
        caretaker.backup()
        
        originator.update_state()
        caretaker.backup()
        
        originator.update_state()
        caretaker.backup()

        caretaker.show_history()
        caretaker.undo()
        caretaker.undo()
        
        caretaker.show_history()

if __name__ == "__main__":
    client = Client()
    client.run_memento()