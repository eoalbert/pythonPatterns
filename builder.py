from __future__ import annotations
from abc import ABC, abstractmethod


class Builder(ABC):

    @abstractmethod
    def build_wall(self):
        pass

    @abstractmethod
    def build_door(self):
        pass

    @abstractmethod
    def build_roof(self):
        pass


class ConcreteBuilderA(Builder):

    def __init__(self):
        self._product = Product()

    @property
    def product(self) -> Product():
        product = self._product
        return product

    def build_wall(self):
        self._product.add("wall_a")

    def build_door(self):
        self._product.add("door_a")

    def build_roof(self):
        self._product.add("roof_a")

    def build_garden(self):
        self._product.add("garden_a")

    def build_house_1(self) -> None:
        self.build_wall()
        self.build_garden()
        self.build_roof()
        self.build_door()


class ConcreteBuilderB(Builder):

    def __init__(self):
        self._product = Product()

    @property
    def product(self) -> Product():
        product = self._product
        return product

    def build_wall(self):
        self._product.add("wall_b")

    def build_door(self):
        self._product.add("door_b")

    def build_roof(self):
        self._product.add("roof_b")

    def build_pool(self):
        self._product.add("pool_b")

    def build_house_1(self) -> None:
        self.build_wall()
        self.build_pool()
        self.build_roof()
        self.build_door()


class Product:

    def __init__(self) -> None:
        self.parts = []

    def add(self, part: str) -> None:
        self.parts.append(part)

    def list_parts(self) ->None:
        print(f"This house has following parts: {','.join(self.parts)}")


class Director:
    def __init__(self) -> None:
        self._builder = None

    @property
    def builder(self) -> None:
        return self._builder

    @builder.setter
    def builder(self, builder: Builder) -> Builder:
        self._builder = builder


if __name__ == "__main__":
    director = Director()
    director.builder = ConcreteBuilderA()
    director.builder.build_house_1()
    director.builder.product.list_parts()

    director.builder = ConcreteBuilderB()
    director.builder.build_house_1()
    director.builder.product.list_parts()
