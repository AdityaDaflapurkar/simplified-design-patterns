class Component:
    def __init__(self, prop1, prop2, prop3, shared_state):
        self.prop1 = prop1
        self.prop2 = prop2
        self.prop3 = prop3
        self._shared_state = shared_state

    def display(self):
        print('Class:Component({}, {}, {},'.format(self.prop1, self.prop2, self.prop3), end=' ')
        self._shared_state.display()
        print(')')

class SharedState:
    def __init__(self, prop1, prop2, prop3, prop4, prop5):
        self.prop1 = prop1
        self.prop2 = prop2
        self.prop3 = prop3
        self.prop4 = prop4
        self.prop5 = prop5

    def display(self):
        print('Class:SharedState({}, {}, {}, {}, {})'.format(self.prop1, self.prop2, self.prop3, self.prop4, self.prop5), end='')

class Client:
    def run_flyweight(self):
        shared_state = SharedState(3, 1, 6, 9, 5)
        objects = []
        for i in range(100):
            objects.append(Component(i, i+1, i+2, shared_state))
        for component in objects:
            component.display()

if __name__ == "__main__":
    client = Client()
    client.run_flyweight()