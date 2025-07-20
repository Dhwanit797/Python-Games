import random

win_count = 0

lose_count = 0

d1 = {"snake": 1, "water": 2, "gun": 3, "end": 4}

while True:
    comp = random.choice([1, 2, 3])
    youstr = input("Select either Snake, Water, Gun, or End to exit the game: ").lower()

    if youstr not in d1:
        print("Invalid choice! Please select correctly!")
        continue

    you = d1[youstr]

    if you == 4:
        print("The game has ended.")
        print(f"Final Score:\nYou Won: {win_count}\nYou Lost: {lose_count}")
        break

    if comp == you:
        print("Draw!!!")
    else:
        if comp == 1 and you == 2:
            print("You choose: water\nComputer choose: snake")
            print("You Lose!!!")
            lose_count += 1

        elif comp == 1 and you == 3:
            print("You choose: gun\nComputer choose: snake")
            print("You Win!!!")
            win_count += 1

        elif comp == 2 and you == 1:
            print("You choose: snake\nComputer choose: water")
            print("You Win!!!")
            win_count += 1

        elif comp == 2 and you == 3:
            print("You choose: gun\nComputer choose: water")
            print("You Lose!!!")
            lose_count += 1

        elif comp == 3 and you == 1:
            print("You choose: snake\nComputer choose: gun")
            print("You Lose!!!")
            lose_count += 1

        elif comp == 3 and you == 2:
            print("You choose: water\nComputer choose: gun")
            print("You Win!!!")
            win_count += 1