import random

print("Winning rules of the Rock Paper scissors game as follows:\n"
      + "Rock vs paper -> paper wins\n"
      + "Rock vs Scissors -> Rock wins\n"
      + "paper vs scissors -> scissor wins\n")

while True:
    print("Enter choice\n 1 for Rock, \n 2 for paper, \n 3 for scissors\n")
    chill = int(input("User turn:"))

    while chill > 3 or chill < 1:
        print("Entered  invalid input, try again ")
        print()
        chill = int(input("User turn : "))
        if chill == 1:
            chill_name = 'Rock'
        elif chill == 2:
            chill_name = 'Paper'
        else:
            chill_name = 'Scissors'
            print('user choice is :' + str(chill))
            print("\n Now is computer turn.....")
    comp_play = random.randint(1, 3)
    while comp_play == chill:
        comp_play = random.randint(1, 3)

    if comp_play == 1:
        comp_chill_name = 'Rock'
    elif comp_play == 2:
        comp_chill_name = 'Paper'
    else:
        comp_chill_name = 'Scissors'

        print("Computer choice is: " + comp_chill_name)
        # print(chill_name + "VS" + comp_chill_name)

    if ((chill == 1 and comp_play == 2) or
            (chill == 2 and comp_play == 1)):
        print("paper wins =>", end=' ')
        result = "paper"
    elif ((chill == 1 and comp_play == 3) or
          (chill == 3 and comp_play == 1)):
        print("Rock wins =>\n", end="")
        result = "ROck"
    else:
        print("scissor wins =>\n", end="")
        result = "scissor"

    # if result == chill_name:
    #     print("==User wins==")
    # else:
    #     print("== Computer wins ==>")
