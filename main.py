class Animal:

    def __init__(self, name, species, legs):
        self.name = name
        self.species = species
        self.legs = legs

    def voice(self):
        pass

    def move(self):
        pass


class Dog(Animal):

    def __init__(self, name, breed):
        super().__init__(name, "Dog", 4) # Я сам знайшов інформацію про використання super та вирішив, що так буде зручніше зробити код
        self.breed = breed

    def bark(self):
        pass


class Bird(Animal):

    def __init__(self, name, wingspan):
        super().__init__(name, "Bird", 2)
        self.wingspan = wingspan

    def fly(self):
        pass


dog = Dog("Jeff", "Labrador")
bird = Bird("Alex", 10)