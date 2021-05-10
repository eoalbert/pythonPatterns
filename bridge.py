from __future__ import annotations
from abc import ABC, abstractmethod


class Model:
    def __init__(self, color):
        self.color = color

    def display_car(self):
        pass


class Ford(Model):
    def __init__(self, color):
        super().__init__(color)

    def display_car(self):
        print(f"This Ford is: {self.color.display()}")


class BMW(Model):
    def __init__(self, color):
        super().__init__(color)

    def display_car(self):
        print(f"This BMW is: {self.color.display()}")


class Color(ABC):

    def display(self):
        pass


class Red(Color):

    def display(self):
        return "red"


class Green(Color):

    def display(self):
        return "green"


class Blue(Color):

    def display(self):
        return "blue"


if __name__ == "__main__":
    color1 = Red()
    color2 = Green()
    color3 = Blue()

    model1 = Ford(color1)
    model1.display_car()

    model2 = BMW(color2)
    model2.display_car()
