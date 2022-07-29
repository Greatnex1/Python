class Person:
    __slots__ = ('name', 'age')

    def __init__(self, name, age):
        self.name = name
        self.age = age

    # def __str__(self):
    #     return f"My name is {self.name}, i am {self.age} years old"

    def __repr__(self):
        return f"Person {self.name}, {self.age}"

    def __eq__(self, other):
        return self.age == other.age

    def __lt__(self, other):
        return self.age < other.age

    def __format__(self, format_spec):
        if format_spec == 'n':
            return self.age
        else:
            return str(self)

    def __len__(self):
        return len(self.name)


person = Person(name="Omotoloa", age=25)
person1 = Person("Ayo", 27)

print(person)
print(f"{person:i}")
print(len(person))

print(person < person1)
