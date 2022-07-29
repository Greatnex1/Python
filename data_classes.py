from dataclasses import dataclass, field

from typing import List, Tuple


# data class gives boiler plate without using the innit a shortcut for constructor creation.
# hey can be overridden.
# how not to re-assign attribute is by using the key word frozen
# once a class is declared as final, it becomes inheritable
# @dataclass(frozen=True)
@dataclass(order=True)
class Human:
    sort_by: Tuple[int, str] = field(init=False, repr=False)
    name: str
    age: int = field(default=0)
    gender: str = field(default="F")
    children: List[str] = field(default_factory=lambda: [], init=False, repr=False)

    #
    #
    # class Human:
    #     def __init__(self, name, age, gender):
    #         self.name = name
    #         self.age = age
    #         self.gender = gender
    #
    def ___post_init___(self):
        self.sort_by = (self.age, self.name)


human = Human("Ojo", 22, "M")

human1 = Human("Dayo", 33, "M")
# x = sorted([human1,human])
# print(x)
human.name = "Dorcas"
print(human)
print(human < human1)
