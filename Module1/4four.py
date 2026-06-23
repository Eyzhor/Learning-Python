name = input("What is your name? ")
birthyear = int(input("What is your birthyear? "))
age = 2026 - birthyear

print(f"Hello {name}, you are {age} years old.")
if age < 18:
    print(f"Years until 18: {18 - age}")
if age >= 18:
    print(f"Years since 18: {age - 18}")