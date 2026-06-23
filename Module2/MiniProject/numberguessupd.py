import random

secret = random.randint(1, 10)
count = 0
won = False

while count < 5:
    while True:
        try:
            guess = int(input("Guess a number between 1 and 10: "))
            if 1 <= guess <= 10:
                break
            print("Please guess between 1 and 10.")
        except ValueError:
            print("Please enter a valid integer.")

    count += 1

    if guess == secret:
        won = True
        break
    elif guess < secret:
        print("Too low!")
    else:
        print("Too high!")

    if count == 5:
        print(f"Game over! The number was {secret}.")

if won:
    print(f"Correct! The number was {secret}.")
    print(f"You got it in {count} attempt{'s' if count != 1 else ''}!")