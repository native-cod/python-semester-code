class Engine:
    def __init__(self, horsepower):
        self.horsepower = horsepower

    def __str__(self):
        return f"The Engines horsepower {self.horsepower}"


class Wheel:
    def __init__(self, size):
        self.size = size

    def __str__(self):
        return f"{self.size} diameter"


class Car:
    engine = None
    wheels = []

    def __init__(self, name, make, year, horsepower, size):
        self.name = name
        self.make = make
        self.year = year
        self.engine = Engine(horsepower)
        # for _ in range(4):
        #     self.wheels.append(Wheel(size))
        self.wheels = [Wheel(size) for _ in range(4)]

    def __str__(self):
        return f"Name : {self.name} Make: {self.make} Year: {self.year} Wheel diameter: {self.wheels[0].size} {self.engine}"


car = Car("BMW m2 Competition", "BMW", 2018, "800HP", "30cm")
print(car)
