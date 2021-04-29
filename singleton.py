class Singleton(type):

    _instances = {}

    def __call__(cls, *args, **kwargs):
        if cls not in cls._instances:
            cls._instances[cls] = super(Singleton, cls).__call__(*args, **kwargs)
        return cls._instances[cls]


class MyClass(metaclass=Singleton):
    def some_business_logic(self):
        pass


if __name__ == "__main__":
    s1 = MyClass()
    s2 = MyClass()

    print(repr(s1))
    print(repr(s2))
