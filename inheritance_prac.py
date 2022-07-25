class Animal:

    def __init__(self, name, breed):
        self.name = name
        self.breed = breed

    def speak(self):
        print("Meows")


class Dog(Animal):
    pass


class Cat(Animal):
    def __init__(self, name, breed, color):
        self.color = color
        super().__init__(name, breed)


cat = Cat("See", "German", "White")
print(cat.name)
print(cat.name)
print(cat.color)

# c = Cat(*vars(cat))
print(vars(cat))
print(cat.speak())
