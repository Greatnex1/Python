

def histogram(word: str) -> dict[str, int]:
    abc = string.ascii_lowercase
    map_ = {}
    for char in abc:
        map_[char] = word.lower().count(char)
    return map_


print(histogram("Alabama"))

print(string.ascii_lowercase)


def histogram_3(word):
    import string
    return {char: word.lower().count(char) for char in string.ascii_lowercase}


print(histogram("No is a language"))
