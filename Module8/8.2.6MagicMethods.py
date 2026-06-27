class Student:
    # Show object format in string format and nicely printed for human reading
    def __str__(
        self,
    ) -> str:
        return "sampat"

    # Show object in technical format required for developer
    def __repr__(self) -> str:
        return "Developer Sampat"


s = Student()

print(s)
print(repr(s))
print([s])
print({s})


class Employee:
    def __init__(self, id, name, age, gender):
        self.__id = id
        self.__name = name
        self.__age = age
        self.__gender = gender

    def __str__(self):
        return f"ID: {self.__id}, name:{self.__name}, age: {self.__age}, gender:{self.__gender}"

    def __repr__(self) -> str:
        return f"Id:{self.__id}, Name:{self.__name}, age:{self.__age}, gender:{self.__gender}"


e = Employee(101, "Sampat", 38, "Male")
print(e)
print([e])
print(repr(e))


class Vector:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def __add__(self, other):
        return f"{self.x+other.x} {self.y+other.y}"

    def __sub__(self, other):
        return f"{self.x-other.x}  {self.y-other.y}"

    def __mul__(self, other):
        return f"{self.x*other.x} {self.y*other.y}"

    def __eq__(self, other):
        return self.x == other.x and self.y == other.y


v1 = Vector(3, 4)
v2 = Vector(2, 3)

print(v1 + v2)
print(v1 - v2)
print(v1 * v2)
print(v1 == v2)
