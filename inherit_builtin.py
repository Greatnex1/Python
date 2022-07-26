from enum import Enum, auto, Flag, unique


class AgeGroup(Enum):
    KID = "kid"
    ADOLESCENT = "teenager"
    ADULT = auto()

#
# print(AgeGroup.ADULT.value)


# OR

@unique
class AgeBracket(Flag):
    KID = 1
    ADOLESCENT = 3
    ADULT = 128


kid = AgeBracket.KID | AgeBracket.ADOLESCENT

print(kid)
