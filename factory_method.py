from __future__ import annotations
from abc import ABC, abstractmethod


class Creator(ABC):

    @abstractmethod
    def create_creator(self):
        pass

    def tell_me_the_animal_name(self):
        product = self.create_creator()
        result = f"{product.tell_name()}"
        return result


class CreateDog(Creator):

    def create_creator(self) -> Product:
        return Dog()


@abstractmethod
class CreateCat(Creator):

    def create_creator(self) -> Product:
        return Cat()


@abstractmethod
class CreateDuck(Creator):

    def create_creator(self) -> Product:
        return Duck()


@abstractmethod
class CreatePigeon(Creator):

    def create_creator(self) -> Product:
        return Pigeon()


class Product(ABC):
    def tell_name(self):
        pass


class Dog(Product):
    def tell_name(self):
        return "Dog"


class Cat(Product):
    def tell_name(self):
        return "Cat"


class Duck(Product):
    def tell_name(self):
        return "Duck"


class Pigeon(Product):
    def tell_name(self):
        return "Pigeon"


def client_code(creator: Creator) -> None:
    print(f"This is an animal, which I do not know what kind but it is a: {creator.tell_me_the_animal_name()}")


if __name__ == "__main__":
    client_code(CreateDog())
    client_code(CreateCat())
    client_code(CreateDuck())
    client_code(CreatePigeon())
