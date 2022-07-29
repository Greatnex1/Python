# iterator is an object that give a value individually

# iterables can become an iterator when the word 'iter is called on it"

hello = iter(["hello,", "how", "are", "you"])

print(next(hello), next(hello), next(hello), next(hello))
# print(next(hello))
# print(next(hello))

# print(list(hello))


class Counter:
    def __init__(self, start, end, step=1):
        self.start = start
        self.end = end
        self.step = step

    def __iter__(self):
        return self

    def __next__(self):
        if self.start < self.end:
            result = self.start
            self.start += self.end
            return result
        else:
            raise StopIteration


counter = Counter(3, 5, 2)
for count in counter:
    print(count)
