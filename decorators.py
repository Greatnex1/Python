# functions are first order objects
# reassign add to an addition variable
# a decorator is a function that returns a function
# a decorator can be used to check the time your code runs
import time
from functools import wraps


def add(a, b):
    return a + b


addition = add
print(addition(4, 6))


# using a method operate to call a function
def operate(a, b, func):
    return func(a, b)


print(operate(6, 4, add))


# a function inside amother function

def funct():
    c = 4

    def func1():
        return c

    return func1()


print(funct())


def plus(a):
    def functi(b):
        return a + b

    return functi


add_3 = plus(6)
print(add_3(7))


def print_decorator(func):
    def wrap(*args, **kwargs):
        print("About to be decorated")
        value = func(*args, **kwargs)
        print("just decorated")
        return value

    return wrap


@print_decorator
def printer():
    return "A printer"


printer()


def timer(func):
    @wraps(func)
    def wrap(*args, **kwargs):
        start = time.perf_counter()
        val = func(*args, **kwargs)
        time_taken = time.perf_counter() - start
        print(f"my {func.__name__} took {time_taken:.2e} to run")
        return val

    return wrap


# @print_decorator
@timer
def factorial(num: int) -> int:

    """
    calculate the factorial value
    :param num:
    :return: factorial value
    """
    import math
    return math.factorial(num)


print(factorial(5))
print(printer())
print(factorial.__doc__)

# a code that shows what time it took to run
