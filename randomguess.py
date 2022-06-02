import random

random_number = random.randint(0, 100)
count = 0
while count < 3:
    guess = int(input("Guess a number :"))
    if guess < random_number:
        print("Too low")
    elif guess > random_number:
        print("Too high")
    else:
        print("Awesome")
        break
    count += 1
else:
    print("You tried")
