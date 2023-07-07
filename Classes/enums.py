#
# define enumerations using Enum base class
#
# use case: for constant declaration
#

from enum import Enum, unique, auto

# we can use unique decorator to avoid duplicate values,
# in this case, the value of APPLE and RED_DELICIOUS cannot be the same
@unique
class Fruit(Enum):
    APPLE = 1
    BANANA = 2
    ORANGE = 3
    TOMATO = 4
    # RED_DELICIOUS = 1 # enum name cannot be the same, but value can be the same

    # if we don't care about the enum value, we can use auto()
    PEAR = auto()


def main():
    # enums have human-readable values and types
    print(Fruit.APPLE)         # Fruit.APPLE
    print(type(Fruit.APPLE))   # <enum 'Fruit'>
    print(repr(Fruit.APPLE))   # <Fruit.APPLE: 1>

    # enums have name and value properties
    print(Fruit.APPLE.name, Fruit.APPLE.value)  # APPLE 1

    # print the auto-generated value
    print(Fruit.PEAR.value)    # 5

    # enums are hashable - can be used as keys
    myFruits = {}
    myFruits[Fruit.BANANA] = "Come Mr. Tally-man"
    print(myFruits)  # {<Fruit.BANANA: 2>: 'Come Mr. Tally-man'}
    print(myFruits[Fruit.BANANA])  # Come Mr. Tally-man


if __name__ == "__main__":
    main()
