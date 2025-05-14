import random

attempts_list = []


def show_score():
    if not attempts_list:
        print("There's currently no high score, start playing!")
    else:
        print(f"The current high score is {min(attempts_list)} attempts")


attempt = 0
random_number = random.randint(1, 10)
print("Hi Player! welcome to the gussing game!")
player_name = input("What's your name? ")
answer = input(
    f"Hi {player_name} would you like to play the guessing game? (Yes/No): "
).lower()
if answer == "no":
    print("Thanks for your time!")
    show_score()
    exit()
else:
    show_score()

while answer == "yes":
    try:
        guess = int(input("pick a number between 1 and 10:"))
        if guess < 1 or guess > 10:
            raise ValueError("Please guess a number within the given range")
        attempt += 1

        if guess == random_number:
            print("Nice, you got it!")
            print(f"It took you {attempt} attempts!")
            answer = input("Would you like to play again (Yes/No): ").lower()
            attempts_list.append(attempt)
            if answer == "no":
                print("That's cool, have a good day.")
            else:
                attempt = 0
                randem_number = random.randint(1, 10)
                show_score()
                continue
        elif guess > random_number:
            print("It's lower!")
        else:
            print("It's higher!")
    except ValueError:
        print("Invalid input! Please enter a number between 1 and 10.")
