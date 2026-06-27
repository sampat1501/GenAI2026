class Vehicle:
    def __init__(self, wheels, doors, windows, fuel_type):
        self.wheels = wheels
        self.doors = doors
        self.windows = windows
        self.fuel_type = fuel_type

    def driving(self):
        print(f"This  is {self.fuel_type} car")


class Tesla(Vehicle):
    def __init__(self, wheels, doors, windows, fuel_type, is_self_driving):
        super().__init__(wheels, doors, windows, fuel_type)
        self.is_self_driving = is_self_driving

    def is_self_driving_car(self):
        print(f"Tesla is self driving car:{self.is_self_driving}")


car1 = Tesla(4, 5, 6, "Electric", True)
car1.driving()
car1.is_self_driving_car()
