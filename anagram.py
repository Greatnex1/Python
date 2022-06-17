number = int(input("Enter a number"))
square_number = number * number
print(square_number)

transform = str(number)
transformer = str(square_number)

inspect = transformer.rfind(transform)

if inspect == 1:
    print("This is an anagram")
else:
    print("Not an anagram")
