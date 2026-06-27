class Person:

    def __init__(self, name, age, gender, account):
        self.__name = name  # private variable
        self.__age = age  # private variable
        self._gender = gender
        self.account = account


def get_age(self):
    print("Gender of the person is {self.__age}")
    return self.gender


p = Person("Sampat", 38, "Male", "HDFC")
print(dir(p))


## Name magling in python


##Private variables
class Employee:
    def __init__(self, name, age, gender, account):
        self.__name = name  # private
        self.__age = age  # Private
        self._gender = gender  # Protected
        self.account = account  # Public


e = Employee("Sampat", 38, "Male", "CBI")
e.__age = 25  ## This will create new variable inside the dictionary with __age=25 and Original variable _Employee__age will remain as is
print(e.__dict__)
print(e._gender)
print(e.__age)


# Encapsulation - Hiding data members and showing the Functionality (Private variables , Public Methods)- In same class
# Abstraction  - Hiding the Implementation and showing only functionality


class Human:
    def __init__(self, name, age, gender):
        self.__name = name
        self.__age = age
        self.__gender = gender

    def get_name(self):
        return self.__name

    def set_name(self, name):
        self.__name = name

    def get_age(self):
        return self.__age

    def set_age(self, age):
        self.__age = age

    def get_gender(self):
        return self.__gender

    def set_gender(self, gender):
        self.__gender = gender


class Employees(Human):
    def __init__(self, name, age, gender):
        super().__init__(name, age, gender)


e = Employees("Rahul", 23, "Male")
employee_name = e.get_name()
print(employee_name)
e.set_name("Sampat")
print(f"The employee name has been set to: {e.get_name()}")
h = Human("Minakshi", 33, "Female")
h_name = h.get_name()
print(f"The Human name is {h_name}")

h_age = h.set_age(30)
print(f"The Human has set age of {h.get_age()}")
