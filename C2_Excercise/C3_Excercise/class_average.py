# initialization phase
total = 0  # sum of grades
grade_counter = 0  # number of grades entered

# processing phase
grade = int(input('Enter score earned, 0 to end: '))
# get one grade
while grade != 0:
    total += grade
    grade_counter += 1
    grade = int(input('Enter score earned, 0 to end: '))
# termination phase
if grade_counter != -1:
    total += grade
    average = total / grade_counter
    print(f'total score of student is {total}')
    print(f'Class average is {average:.2f}')

else:
    print('No grades were entered')
