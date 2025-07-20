import random

comp = random.randint(1,6)
no_of_guesses = 0 

while True:
    user_guess = int(input("Enter a number : "))
    no_of_guesses += 1

    if user_guess == comp:
        print("You died !!!")
        print(f"Number of guesses : {no_of_guesses}")
        break

    else:
        print("You are safe !!!")