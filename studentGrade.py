numberOfSub = int(input("Enter numbers of subject : "))
numberOfStud = int(input("Enter number of student : "))

print()

sub = [input(f"Enter subject{i} title :") for i in range(1, numberOfSub + 1)]

print()

storage = []

for b in range(1, numberOfStud + 1):
    studentName = input("Enter name of student ")
    subject_name = input("Enter subject name")
    subs = input("Enter subject name")
    sub_score = [int(input(f"Enter {studentName} score for {subject_name} : ")) for numberOfSub in
                 range(1, numberOfStud + sub)]
    total = sum(sub_score)
    average = total / len(sub)
    # print(total)
    # print(average)

    info = {"student": studentName,
            "subject score :": sub_score,
            "total score": total,
            "average score": average}

    storage.append(info)
    print()

avg_score = [n["average score"] for n in storage]
student_name = [n["student"] for n in storage]
total_score = [int(n["total score"]) for n in storage]

print(avg_score)

# how to print dates in python
# #
# import datetime
#
# x = datetime.datetime.now()
#
# print(x.year)
# print(x.strftime("%A"))


# using numbers as index placeholder
# quantity = 3
# itemno = 567
# price = 49
# myorder = "I want {0} pieces of item number {1} for {2:.2f} dollars."
# print(myorder.format(quantity, itemno, price))
