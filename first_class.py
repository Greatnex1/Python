# class MyClass:
#     var = "I am here to explore"
#
#
# first = MyClass()
# second = MyClass()
#
# print(first)
#
# first.var = "Hello World!"
#
# print(first.var)
# print(second.var)
#
#
# # all instance method has a (self)
#
# class Myclass:
#     def method(self):
#         pass
#
#
# mine = Myclass()
# mine.method()
# from typing import Self

# Decorator affects how a class works

class Person:
    persons = 0

    def __init__(self, Person_name: str) -> None:
        self._Person_name = Person_name
        self._age__ = 17
        Person.persons += 1

    @classmethod
    def getpersons(cls):
        return cls.persons

    @staticmethod
    def determine_class(age: int) -> str:
        if age >= 18:
            return "Major"
        return "Minor"

    # @property

    # def name(self):
    #     return self._Person_name
    #
    # @name.setter
    # def name(self, new_name):
    #     self._Person_name = new_name

    @property
    def age(self):
        return self._age__

    @age.setter
    def age(self, new_age):
        if new_age < 0:
            raise ValueError("Age is too low")
        self._age__ = new_age

    @property
    def name(self):
        return self._Person_name

    @name.setter
    def name(self, new_name):
        self._Person_name = new_name

    @name.deleter
    def name(self):
        print("Name won't be deleted")
        del self._Person_name


person1 = Person("Joy")
# print(person1.age)
person1._Person_name = "Will"
# del person1.name
# person1.age = -2
# print(person1.age)
print(Person.determine_class(12))

# print(person1.persons)
# # person1.Person_name = "Omo f"
# print(person1.Person_name_)
# print(person1._age__)
# print(dir(person1))
# print(person1._age__)

# when naming a variable as private give it an under_score
