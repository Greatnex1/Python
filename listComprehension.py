# lst = [i for i in range(1, 11)]
#
# print(lst)
# # check for even numbers using loops
# b_lst = [i ** 2 for i in range(1, 11) if i % 2 == 0]
#
# print(b_lst)
#
# eo_list = ["even" if 3 % 2 == 0 else "odd"]
#
# print(eo_list)
#
# c_list = [i // 2 for i in range(2, 100) if i % 2 == 1]
#
# print(c_list)
#
# eos_list = [j ** 2 if j % 2 == 0 else j for j in range(1, 11)]
#
# print(eos_list)
#
# names = ["Ade"], ["Wills"]
# # Sum = [int(input("Enter a score :")) for i in range(1, 10)]
# total = sum(int(input("Enter score :")) for i in range(1, 10))
# # print(Sum)
# print(total)


def is_prime(num: int) -> bool:
    import math
    max_divisor = math.ceil(math.sqrt(num))
    # max_divisor = (num // 2) + 1
    for i in range(2, max_divisor):
        if num % i == 0:
            return False

    return True


print(is_prime(7))


def cube(num: int) -> int:
    return num ** 3


cubes = [cube(i) for i in range(1, 11)]

print(cubes)
