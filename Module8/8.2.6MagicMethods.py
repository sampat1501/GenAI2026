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
