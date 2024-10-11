number_grade = int(input("Enter a numerical grade between 0 - 100: "))

if number_grade.isdigit():
    if 80 <= number_grade <= 100:
        print(f"Your grade is: A")
    elif 60 <= number_grade <= 79:
        print(f"Your grade is: B")
    elif 50 <= number_grade <= 59:
        print(f"Your grade is: C")
    elif 40 <= number_grade <= 49:
        print(f"Your grade is: D")
    elif 0 <= number_grade <= 39:
        print(f"Your grade is: F")
    else:
        print("Error: Grades must be between 0 and 100")
    
else:
    print("Error: Please enter a number")
