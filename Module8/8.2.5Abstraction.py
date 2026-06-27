from abc import ABC, abstractmethod


# Unimplemented and implemented methods
class Vehicle(ABC):
    @abstractmethod
    def start(self):
        pass

    @abstractmethod
    def wheels(self):
        pass

    @abstractmethod
    def engine(self):
        pass

    @abstractmethod
    def doors(self):
        pass

    def drive(self):
        return "Honda city have only front wheel drive system"


class HondaCity(Vehicle):
    def start(self):
        return "Honda city 2 options , button start and key start"

    def doors(self):
        return "Honda city has 4 nice doors"

    def engine(self):
        return "Honda city has 2 engine options , Petrol and diesel"

    def wheels(self):
        return "Honda city is only hace four wheel options and 02 wheel drive"


hc = HondaCity()
starting = hc.start()
print(starting)
