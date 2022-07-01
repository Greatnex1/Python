# def get_digit(number, position):
#     return number // (10 ** position) % 10
#
#
# numbers = get_digit(3456789, 5)
# print(numbers)
#
# print("Hello", end='')
# print(" My Friend")
#
#
# def appender(lst=None):
#     if lst is None:
#         lst = []
#     # lst.append("You")
#     lst.insert(1, "You")
#     return lst
#
#
# print(appender([]))
# print(appender(["You"]))
# print(appender([1, 3, 5, ]))

#
# def sub(a: int = 0, b: int = 0) -> int:
#     """Cal the difference between
#
#     ++++++++++++++
#     **************
#
#     ****
#
#     """
#     return b - a
#
#
# print(sub(b=10, a=15))
# print(sub.__annotations__)
# print(sub.__doc__)

# tuple packing
def avg(*args):
    from statistics import mean
    # total = 0
    # for i in args:
    #     total +=1
    return mean(args)
    # print(type(args))


# return args

print(avg(2, 4, 6, 7))

lst = [1, 5, 7, 8, 9]

set_ = [3, 4, 5]
print(avg(*lst))
print(avg(*set_))


def divide(x=0, y=0) -> int:
    return y // x


print(divide(2, 10))

# appender = 0['you']
#

#
#  l + y
# [3, 4, 5, 6, 7, 6, 7, 7]
# >>> len(y)
# 3
# >>> len(l)
# 5
# >>> 2 in l
# False
# >>> words = "AinaWIlliams"
# >>> list(words)
# ['A', 'i', 'n', 'a', 'W', 'I', 'l', 'l', 'i', 'a', 'm', 's']
# >>> words[0:6]
# 'AinaWI'

#
# List is a collection which is ordered and changeable. Allows duplicate members.
# Tuple is a collection which is ordered and unchangeable. Allows duplicate members.
# Set is a collection which is unordered, unchangeable*, and unindexed. No duplicate members.
# Dictionary is a collection which is ordered** and changeable. No duplicate members.
