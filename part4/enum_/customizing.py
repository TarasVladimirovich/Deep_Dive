from enum import Enum


class Color(Enum):
    red = 1
    green = 2
    blue = 3

    def pure_color(self, value):
        return {self: value}

    def __repr__(self):
        return f'{self.name} ({self.value})'


print(Color.red.pure_color(100), Color.blue.pure_color(200))
print(Color.red)


class Number(Enum):
    ONE = 1
    TWO = 2
    THREE = 3

    def __lt__(self, other):
        return isinstance(other, Number) and self.value < other.value

    def __eq__(self, other):
        if isinstance(other, Number):
            return self is other
        elif isinstance(other, int):
            return self.value == other
        else:
            return False


try:
    Number.ONE > Number.TWO
except TypeError as ex:
    print(ex)
