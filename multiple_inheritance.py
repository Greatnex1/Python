# class A:
#     def do_this(self):
#         print("From a")
#
#
# class C(A):
#     def do_this(self):
#         print("From a")
#
#
# class B(C):
#     def do_this(self):
#         print("From C")
#
#
# class D(B, C):
#     def do_this(self):
#         print("From D")
#
#
# print(help(D))

import abc


class Animalia(abc.ABC):
    __metaclass__ = abc.ABCMeta

    def name(self):
        print("Bull")

    # @abc.abstractmethod
    def speak(self):
        return


class Dog(Animalia):
    def speak(self):
        print("Bow bow ")


class Cat(Animalia):
    def speak(self):
        print("meow")


cat = Cat()
dog = Dog()
print(cat.speak())
print(dog.name())
