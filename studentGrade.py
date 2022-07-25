numberOfSub = int(input("Enter numbers of subject : "))
numberOfStud = int(input("Enter number of student : "))
print()
sub = [input(f"Enter subject {i + 1} title :") for i in range(0, numberOfSub)]

print()

storage = []
for b in range(0, numberOfStud):
    print()
    studentName = input("Enter name of student ")
    # subject_name = input("Enter name of subject")
    # sub_score = [int(input(f"Enter {studentName} score for {sub[b]}  :")) for numberOfSub in
    #              range(1, numberOfStud + 1)]
    sub_scores = (int(input(f"Enter {studentName}'s score for {every_sub}  :")) for every_sub in sub)
    # subs = input(f"Enter {studentName} score for physics :")
    # subs = input(f"Enter {studentName} score for maths :")

    total = sum(sub_scores)
    average = total / len(sub)
    # print(total)
    # print(average)
    info = {"student": studentName,
            "subject score": sub_scores,
            "total score": total,
            "average score": average}

    storage.append(info)
    # print(storage)

avg_score = [n["average score"] for n in storage]
student_name = [n["student"] for n in storage]
total_score = [int(n["total score"]) for n in storage]
sub_scores = [n["subject score"] for n in storage]

print("========================================================================")
print("             STUDENT GRADE REPORT OF SEMICOLON NATIVE ENGINEERS                 ")
print("=======================================================================")
# """STUDENT  SUBJECT     SCORES  TOTAL   AVERAGE"""

print('Name',               'Subject',      'Total',     'Average')
print(studentName,   sub,    total,     average)

# for i in range(0, numberOfSub):

for i in range(0, numberOfStud):
    print(student_name[i])

# for i in range(0, len(storage)):
#     print(f" {student_name[i]}      {total_score[i]}    {avg_score[i]}")

# print("Hello", end='')
# ...

# print(student_name)
# print(total_score)
# print(avg_score)
#
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
