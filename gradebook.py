#Get score input
grade = int(input("What is your grade?"))

#grade the score
if grade >= 90:
    print('Your grade is an "A"')
elif grade >= 80:
    print('Your grade is a "B"')
elif grade >= 70:
    print('Your grade is a "C"')
elif grade >= 60:
    print('Your grade is a "D"')
else:
    print('Your grade is an "F"')