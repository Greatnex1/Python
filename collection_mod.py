import collections

word = collections.Counter("Amaka")
print(word)

print(word.most_common(1))
print(word.subtract(word))
