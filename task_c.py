password = input("Enter a password containing only letters and numbers: ")

numbers = password.isdigit()
letters = password.isalpha()

if len(password) >= 8 and numbers == False and letters == False:
    print("Your password is valid")
else:
    print("Your password must contain at least 8 characters, and a mix of letters and numbers")