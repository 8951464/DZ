class Kingdom:
#царство живых организмов
    def __init__(self, name):
    self.name = name


class Animal(Kingdom):
    def __init__(self, food, shit):
        super().__init__('Animal')
        self.food = food
        self.shit = shit


class Doggy(Animal):
    def __init__(self, type):
        super().__init__(10, 5)
        self.type = type

Sharik=Doggy('Bulgod')

