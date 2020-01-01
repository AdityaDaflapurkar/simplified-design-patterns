from abc import ABC, abstractmethod
class Iterator(ABC):
    @abstractmethod
    def next(self):
        pass

    @abstractmethod
    def has_next(self):
        pass

class ConcreteIterator:
    def __init__(self, collection):
        self._collection = collection
        self._index = 0
    
    def next(self):
        item = self._collection.get_items()[self._index]
        self._index += 1
        return item

    def has_next(self):
        return self._collection.get_count() > self._index



class Collection(ABC):
    @abstractmethod
    def add(self, element):
        pass

    @abstractmethod
    def remove(self, element):
        pass

    @abstractmethod
    def get_iterator(self):
        pass

class ConcreteCollection(Collection):
    def __init__(self):
        self._items = []

    def add(self, element):
        self._items.append(element)

    def remove(self):
        self._items.pop()

    def get_iterator(self):
        return ConcreteIterator(self)

    def get_items(self):
        return self._items

    def get_count(self):
        return len(self._items)

class Client:
    def run_iterator(self):
        collection = ConcreteCollection()
        collection.add(1)
        collection.add(3)
        collection.add(7)
        collection.add(4)
        collection.add(6)
        it = collection.get_iterator()
        while it.has_next():
            print(it.next())

if __name__ == "__main__":
    client = Client()
    client.run_iterator()