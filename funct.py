def get_digit(number, position):
    return number // (10 ** position) % 10


numbers = get_digit(3456789, 5)
print(numbers)


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
