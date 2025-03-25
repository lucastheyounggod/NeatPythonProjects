import random
import string

def generate_password(length = 12, include_special = False):
    characters = string.ascii_letters + string.digits
    if include_special:
        characters += string.punctuation

    password = ''.join(random.choice(characters) for _ in range(length))
    return password

#Ask the user for password length
while True:
    try:
        length = int(input("Enter the password length: "))
        if length < 6:
            print("Password should be at least 6 characters long for security")
            continue

        special = input("Include special characters? (Yes/No): ").strip().lower()
        include_special = special in ["yes", "y"]

        print("\nGenerated Password: ", generate_password(length, include_special) )
        break

    except ValueError:
        print("Invalid input! Please enter a number.")