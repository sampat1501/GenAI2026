class Father:
    def __init__(self, money, house, estate):
        self.money = money
        self.house = house
        self.estate = estate

    def get_house(self):
        print(f"We got {self.house} from father by inheritance")


class Mother:
    def __init__(self, love, food, care):
        self.love = love
        self.food = food
        self.care = care

    def mothers_love(self):
        print(f"Mother by giving {self.love} to us")


class Child(Father, Mother):

    def __init__(self, money, house, estate, love, food, care, earning):
        Father.__init__(self, money, house, estate)
        Mother.__init__(self, love, food, care)
        self.earning = earning

    def my_earnings(self):
        print(f"My earning per month is:  {self.earning}")


child = Child(
    100000,
    "CA House",
    "Land of 4 Acre",
    "Lots of love",
    "Mutton",
    "Giving Food",
    1000000,
)
child.get_house()
child.mothers_love()
child.my_earnings()
