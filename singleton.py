class Singleton(type):
    """
    Define an Instance operation that lets clients access its unique
    instance.
    """
    def __init__(cls, name, bases, attrs, **kwargs):
        super().__init__(name, bases, attrs)
        cls.foo = None

    def __call__(cls, *args, **kwargs):
        if cls.foo is None:
            cls.foo = super().__call__(*args, **kwargs)
        return cls.foo


class SingletonCandidate(metaclass=Singleton):
    """
    Example class.
    """

    pass


def main():
    s1 = SingletonCandidate()
    s2 = SingletonCandidate()
    assert s1 is s2


if __name__ == "__main__":
    main()
