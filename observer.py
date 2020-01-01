from abc import ABC, abstractmethod
class Subject(ABC):
    @abstractmethod
    def subscribe(self, observer) -> None:
        pass

    @abstractmethod
    def unsubscribe(self, observer) -> None:
        pass

    @abstractmethod
    def broadcast(self) -> None:
        pass


class ConcreteSubject(Subject):
    def __init__(self):
        self._state = 0
        self._observers = []
        
    def subscribe(self, observer) -> None:
        self._observers.append(observer)

    def unsubscribe(self, observer) -> None:
        self._observers.remove(observer)

    def broadcast(self) -> None:
        for observer in self._observers:
            observer.update(self)

    def update_state(self, new_state) -> None:
        self._state = new_state
        print('ConcreteSubject()::update_state({})'.format(self._state))
        self.broadcast()
    
    def get_state(self):
        return self._state 

class Observer(ABC):

    @abstractmethod
    def update(self, subject: Subject) -> None:
        pass



class ConcreteObserver1(Observer):
    def update(self, subject: Subject) -> None:
        print('ConcreteObserver1()::update()::state={}'.format(subject.get_state()))


class ConcreteObserver2(Observer):
    def update(self, subject: Subject) -> None:
        print('ConcreteObserver2()::update()::state={}'.format(subject.get_state()))


class Client:
    def run_observer(self):

        subject = ConcreteSubject()

        observer1 = ConcreteObserver1()
        subject.subscribe(observer1)

        observer2 = ConcreteObserver2()
        subject.subscribe(observer2)

        subject.update_state(1)
        subject.update_state('Hello')

        subject.unsubscribe(observer1)

        subject.update_state(3.14)


if __name__ == "__main__":
    client = Client()
    client.run_observer()