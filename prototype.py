from __future__ import annotations
from abc import ABC, abstractmethod
import copy


class IPrototype(ABC):

    @staticmethod
    @abstractmethod
    def clone(mode):
        pass


class MyPrototype(IPrototype):

    def __init__(self, lst):
        self.list = lst

    def clone(self, mode):
        new_list = []

        if mode == "shallow copy":
            print("creating a shallow copy...")
            new_list = self.list.copy()

        if mode == "deep copy":
            print("creating a deep copy...")
            new_list = copy.deepcopy(self.list)

        return type(self)(
            new_list
        )

    def print_list(self):
        print(f"{id(self)}\tlist={self.list}")


if __name__ == "__main__":
    original = MyPrototype([[1, 2, 3], [4, 5, 6]])
    original.print_list()

    copy_1 = original.clone("shallow copy")
    copy_1.list[1] = [10, 20, 30]
    original.print_list()
    copy_1.print_list()

    copy_1 = original.clone("shallow copy")
    copy_1.list[1][0] = 50
    original.print_list()
    copy_1.print_list()

    copy_1 = original.clone("deep copy")
    copy_1.list[1] = [20, 40, 60]
    original.print_list()
    copy_1.print_list()

    copy_1 = original.clone("deep copy")
    copy_1.list[1][0] = 100
    original.print_list()
    copy_1.print_list()
