number_grade = input("Enter a numerical grade between 0 - 100: ")
if not number_grade.isdigit():
    print("Error: Please enter a number")
else:
    number_grade = int(number_grade)
    if 80 <= number_grade <= 100:
        print("Your grade is: A")
    elif 60 <= number_grade <= 79:
        print("Your grade is: B")
    elif 50 <= number_grade <= 59:
        print("Your grade is: C")
    elif 40 <= number_grade <= 49:
        print("Your grade is: D")
    elif 0 <= number_grade <= 39:
        print("Your grade is: F")
    else:
        print("Error: Grades must be between 0 and 100")
    
