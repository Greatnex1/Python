# def twoSum(listofnumbers, target) -> int:
#     list = [3, 1, 5, -8], 6
#
#
#     return 0 ,1

# doctest
from __future__ import annotations

from typing import Union


def duals(lists_of_numbers: list, target: int) -> list:
    for i in range(len(lists_of_numbers) - 1):
        for j in range(i + 1, len(lists_of_numbers)):
            num = lists_of_numbers[i] + lists_of_numbers[j]

            if target == num:
                return [i, j]

    return []


def dual1(lists_of_numbers: list, target: int) -> list | str | int:
    map_ = {}
    for i in range(len(lists_of_numbers)):
        comple = target - lists_of_numbers[i]

        if comple in map_:
            return [map_[comple], i]
        else:
            map_[lists_of_numbers[i]] = i

    # return []
    # return -1
    return "Null"


print(dual1([1, 3, 5, -8, 3], 7))
