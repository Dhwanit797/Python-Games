import random

comp = random.randint(1, 100)
no_of_guesses = 0

while True:
    user_guess = int(input("Enter a number between 1 to 100: "))

    if user_guess > 100 or user_guess < 1:
        print("Please enter a valid number between 1 and 100.")
        continue

    no_of_guesses += 1

    if user_guess == comp:
        print("Bravo !!! You guessed it right!")
        print("Number of guesses:", no_of_guesses)
        break
    elif user_guess > comp:
        print("Too high! Try again.")
    else:
        print("Too low! Try again.")