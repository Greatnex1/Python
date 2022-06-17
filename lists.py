import random

print("Welcome to number lists")

lst = [4, 5, 6, 7, 8]

ranger = list(range(1, 100, 5))
print(ranger)
#
# ranger.append(1_000)
# print(ranger)
# # extend is the same to "+="
# ranger.extend([5, 7, 8])
# print(ranger)
#
# ranger.append([5, 6, 7])
# print(ranger)
#
# ranger.insert(0, 64)
# print(ranger)
#
# popped = ranger.pop(10)
# print(popped)
# print(ranger)
#
# lst = ranger[:]
# ranger.clear()
#
# random.shuffle(ranger)
# print(ranger)
#
# ranger.sort(reverse=True)
# print(ranger)
#
# fruit = ["apple", "mango", "pine", "cherry", "orange"]
# fruit.sort()
# print(fruit)
#
# fruit.sort(key=len, reverse=True)
# print(fruit)
# prime = list(range(2, 100, 2))
# prime_list = [2, 3, 5, 7, 11, 13, 17, 19, 23, 29, 31, 37, 41, 43, 47, 53, 59, 61, 67, 71, 73, 79, 83, 89, 97]
# print(prime_list)
# print(list(prime))

# for num in list(range(2, 101 + 1)):
#
#     if num > 1:
#
#         for i in list(range(2, num)):
#             if (num % i) == 0:
#                 break
#         else:
#
#             print(num)


primes = [i for i in range(2, 101) if i % 2 != 0]
print(primes)

#
# n = 20
# primes = []
#
# for num in range(2, 100 + 1):
#
#     if num > 1:
#         for i in range(2, num):
#             break
#     else:
#         primes.append(i)
# num = primes
# print(primes)

# def rotate_list(list, k)

joy = "{{("")[45]}}"
print(joy)

'[({)]'

# print(id(ranger))
# print(id(lst))
# print()

names = ["Hello"]

camel = names.append(["Dear"])
print(names)
