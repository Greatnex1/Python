# def rotate(lst, k):
#     # k = k % len(lst)
#
#     return lst[k:] + lst[:k]
#
#
# print(rotate([1, 3, 5, 7, 8, 9, 0], 1))
# print(rotate([1, 3, 5, 7, 8, 9, 0], 2))
# print(rotate([1, 3, 5, 7, 8, -9, 0], 80))
# print(rotate(["joy", 1, "happiness", 2, "Will"], -1))
#


# LIFO
def bracket_pair(brackets: str) -> bool:
    if len(brackets) < 2 or len(brackets) % 2 != 0:
        return False

    arrange = []
    for bracket in brackets:
        if bracket in "{[(":
            arrange.append(bracket)


        elif bracket in "]})":
            peek = arrange[-1]
            if (bracket == "(" and peek == ")") or \
                    (bracket == "[" and peek == "]") or \
                    (bracket == "{" and peek == "}"):
                arrange.pop()
            else:
                return False

        else:
            return False
        return True


print(bracket_pair("{}{([]})"))

"{}({[]})"

#
# lst = [7, -4, 4, 9]
# w = 2
#
# print(rotate(2, w))
