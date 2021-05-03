from __future__ import annotations


class ModuleA:

    def request(self) -> str:
        return "ModuleA: This is an input String"


class ModuleB:

    def specific_request(self) -> str:
        return "B eludom morf gnirts a si sihT"


class Adapter(ModuleA, ModuleB):

    def request(self) -> str:
        return f"Adapter: {self.specific_request()[::-1]}"


def client_code(module_a: ModuleA) -> None:
    print(module_a.request(), end="")


if __name__ == "__main__":
    module_a = ModuleA()
    client_code(module_a)
    print("\n")

    module_b = ModuleB()
    print(f"ModuleB: {module_b.specific_request()}", end="\n\n")

    print("Translated")
    adapter = Adapter()
    client_code(adapter)
