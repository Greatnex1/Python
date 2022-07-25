class Dog:
    # An object is mutable if it can be altered dynamically
    # Class Attribute
    # __str__() this method is known as the dunder method because they begin and end with double underscores
    # a variable is declared private by using an underscore e.g name_
    species = "Canis familiaris"

    def __init__(self, name, age, color):
        self.name = name
        self.age = age
        self.color = color

    # Instance method
    # def __str__(self):
    #     return f"{self.name} is {self.age} years old says {self.color}"

    def __str__(self):
        return f"{self.name}'s coat is {self.color}"

    def description(self):
        return f"{self.name} is {self.age} years old"

    def color(self, color):
        return f"{self.name}'s color is {color}"


Dog1 = Dog("German Shepherd", 26, "Ash")

# print(Dog1.name)
# # print(Dog1.description())
# print(Dog1.speak("Woof woof"))
print(f"{Dog1.name}'s coat is {Dog1.color}")
print(Dog1)

Dog2 = Dog("Wolf", 33, "Wof")
