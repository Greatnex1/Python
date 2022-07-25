class Car:
    color = "Grey"
    miles = 20_000

    def __init__(self, color, miles):
        self.color = color
        self.miles = miles

    def __str__(self):
        return f"The {self.color} car has {self.miles} miles."

    def drive(self, number):
        return number


Car1 = Car("Blue", "20,000")
Car2 = Car("Red", "30,000")

print(Car1)
print(Car2)
print(Car2.drive(0))