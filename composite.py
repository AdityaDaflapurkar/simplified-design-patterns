from abc import ABC, abstractmethod

class Component(ABC):
    def __init__(self, value):
        self._value = value

    def add_child(self, component):
        pass

    def remove_child(self, component):
        pass

    def has_children(self):
        return False

    @abstractmethod
    def method1(self):
        pass


class Leaf(Component):
    def method1(self):
        print(self._value)


class Composite(Component):
    def __init__(self, value):
        self._value = value
        self._children = []

    def add_child(self, component):
        self._children.append(component)
        component.parent = self

    def remove_child(self, component):
        self._children.remove(component)
        component.parent = None

    def has_children(self):
        return True

    def method1(self):
        print(self._value)
        for child in self._children:
            child.method1()

class Client:
    def run_composite(self, component:Component):
        component.method1()

if __name__ == "__main__":
    tree = Composite(1)

    branch1 = Composite(2)
    branch1.add_child(Leaf(3))
    branch1.add_child(Leaf(4))

    branch2 = Composite(5)
    branch2.add_child(Leaf(6))

    tree.add_child(branch1)
    tree.add_child(branch2)

    client = Client()
    client.run_composite(tree)
