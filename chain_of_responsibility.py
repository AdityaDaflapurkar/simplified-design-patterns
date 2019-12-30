
from abc import ABC, abstractmethod

class Handler(ABC):
    @abstractmethod
    def set_next(self, handler):
        pass

    @abstractmethod
    def handle(self, request):
        pass


class AbstractHandler(Handler):

    _next = None

    def set_next(self, handler: Handler) -> Handler:
        self._next = handler
        # Returning a handler from here will let us link handlers in a
        # convenient way like this:
        # monkey.set_next(squirrel).set_next(dog)
        return handler

    @abstractmethod
    def handle(self, request):
        if self._next:
            return self._next.handle(request)

        return None

class ConcreteHandler1(AbstractHandler):
    def handle(self, request):
        if request == '1':
            return 'Request handled by ConcreteHandler1'
        else:
            return super().handle(request)


class ConcreteHandler2(AbstractHandler):
    def handle(self, request):
        if request == '2':
            return 'Request handled by ConcreteHandler2'
        else:
            return super().handle(request)


class ConcreteHandler3(AbstractHandler):
    def handle(self, request):
        if request == '3':
            return 'Request handled by ConcreteHandler3'
        else:
            return super().handle(request)

class ConcreteHandler4(AbstractHandler):
    def handle(self, request):
        if request == '4':
            return 'Request handled by ConcreteHandler4'
        else:
            return super().handle(request)

class Client:
    def run_chain_of_responsibility(self, handler: Handler):
        for request in ['4', '1', '3', '2', '2', '5']:
            result = handler.handle(request)
            if result:
                print('{}'.format(result))
            else:
                print('Request {} not handled'.format(request))

if __name__ == "__main__":
    h1 = ConcreteHandler1()
    h2 = ConcreteHandler2()
    h3 = ConcreteHandler3()
    h4 = ConcreteHandler4()
    h1.set_next(h2).set_next(h3).set_next(h4)

    client = Client()
    client.run_chain_of_responsibility(h1)


