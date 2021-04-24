from __future__ import annotations
from abc import ABC, abstractmethod


class Family(ABC):

    @abstractmethod
    def create_mom(self) -> Mom:
        pass

    @abstractmethod
    def create_dad(self) -> Dad:
        pass

    @abstractmethod
    def create_child(self) -> Child:
        pass


class FamilySchmidt(Family):

    def __init__(self):
        print("Calling family Schmidt")

    def create_mom(self) -> Mom:
        return MomSchmidt()

    def create_dad(self) -> Dad:
        return DadSchmidt()

    def create_child(self) -> Child:
        return ChildSchmidt()


class FamilyWilly(Family):

    def __init__(self):
        print("Calling family Willy")

    def create_mom(self) -> Mom:
        return MomWilly()

    def create_dad(self) -> Dad:
        return DadWilly()

    def create_child(self) -> Child:
        return ChildWilly()


class FamilyDonald(Family):

    def __init__(self):
        print("Calling family Donald")

    def create_mom(self) -> Mom:
        return MomDonald()

    def create_dad(self) -> Dad:
        return DadDonald()

    def create_child(self) -> Child:
        return ChildDonald()


class Mom(ABC):

    @abstractmethod
    def say_name(self):
        pass


class Dad(ABC):

    @abstractmethod
    def say_name(self):
        pass


class Child(ABC):

    @abstractmethod
    def say_name(self):
        pass


class MomSchmidt(Mom):
    def say_name(self):
        return "Mortisha"


class DadSchmidt(Mom):
    def say_name(self):
        return "Jimmy"


class ChildSchmidt(Mom):
    def say_name(self):
        return "Fluffy"


class MomWilly(Mom):
    def say_name(self):
        return "Yuhu"


class DadWilly(Mom):
    def say_name(self):
        return "Peter"

class ChildWilly(Mom):
    def say_name(self):
        return "Stewy"


class MomDonald(Mom):
    def say_name(self):
        return "Jasmin"


class DadDonald(Mom):
    def say_name(self):
        return "Griffin"


class ChildDonald(Mom):
    def say_name(self):
        return "Lara"


def client_code(family: Family) -> None:
    mom = family.create_mom()
    dad = family.create_dad()
    child = family.create_child()

    print(f"Mom's name is {mom.say_name()}")
    print(f"Dad's name is {dad.say_name()}")
    print(f"Child's name is {child.say_name()}")
    print(" ")


if __name__ == "__main__":
    client_code(FamilySchmidt())
    client_code(FamilyWilly())
    client_code(FamilyDonald())