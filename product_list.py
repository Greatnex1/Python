a_list = list(range(1, 100, 1))
multiplied_list = [element ** 2 for element in a_list]
print(a_list)
print(multiplied_list)
#
# word = "I love me"
# word_split = word.split()
# print(word_split)
# ex = " ".join(word_split)
# print(ex)
#
# b_list = [1, 2, [4, 5], 7]
#
# b_list_copy = b_list[:]
#
# print(b_list_copy)
#
# b_list[2][0] = 10
#
# print(b_list)

# tupleMEhod
print()
t = (1, 2, [3, 4])
t[2].append(6)
print(t)
