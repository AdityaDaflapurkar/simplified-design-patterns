from abc import ABC, abstractmethod


class Component(ABC):

    @abstractmethod
    def request(self):
        pass


class RealComponent(Component):
    def request(self) -> None:
        print("RealComponent: Handling request.")


class ProxyComponent(Component):
    def __init__(self, real_component: RealComponent) -> None:
        self._real_component = real_component

    def request(self):
        if self.check_access():
            self._real_component.request()
            self.log_access()

    def check_access(self) -> bool:
        print("Proxy: Checking access prior to firing a real request.")
        return True

    def log_access(self) -> None:
        print("Proxy: Logging the time of request.")


class Client:
    def run_proxy(self, component: Component):
        component.request()


if __name__ == "__main__":
    real = RealComponent()
    proxy = ProxyComponent(real)
    client = Client()
    client.run_proxy(proxy)