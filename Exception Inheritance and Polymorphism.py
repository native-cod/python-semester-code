# A custom Exception [ line 3 : 7 ]
class MyTypeError(Exception):
    def __init__(self, message):
        self.message = message
        super().__init__(message)


class Addition:
    @classmethod
    def addition(cls, x, y):
        return x + y


class Subtraction:
    @classmethod
    def subtraction(cls, x, y):
        return x - y


class Multiplication:
    @classmethod
    def product(cls, x, y):
        return x * y


class Division:
    @classmethod
    def division(cls, x, y):
        return x / y


# Multiple Inheritance
class Calculator(Addition, Subtraction, Multiplication, Division):

    # additional method to the child class included with a custom exception for typeError
    @classmethod
    def abs(cls, value):
        if isinstance(value, int):
            if value < 0:
                return value * -1
            else:
                return value
        else:
            raise MyTypeError("Only numeral values can be passed to this function as arguments")


calc = Calculator()
# Exception handling for our "abs" method from Calculator class [ line 50 : 53 ]
try:
    calc.abs("welcome")
except MyTypeError as e:
    print(e)


class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def __repr__(self):
        return "{}, {} Details of the person".format(self.name, self.age)

    def __str__(self):
        return "{}, {}".format(self.name, self.age)


# Polymorphism Operator overloading for + - x and division operators
class Point:

    def __init__(self, x, y):
        self.x = x
        self.y = y

    # operator overloading
    def __add__(self, other):
        result = f"({self.x + other.x} {self.y + other.y})"
        return result

    def __sub__(self, other):
        result = f"({self.x - other.x} {self.y - other.y})"
        return result

    def __mul__(self, other):
        result = f"({self.x * other.x} {self.y * other.y})"
        return result

    def __truediv__(self, other):
        result = f"({self.x / other.x} {self.y / other.y})"
        return result

    def __str__(self):
        return "({}, {})".format(self.x, self.y)


point_1 = Point(2, 3)
point_2 = Point(4, 5)

print(point_1.__add__(point_2))
print(point_1 + point_2)
print(point_1 / point_2)
print(point_1.__str__())
