import random


def get_user_choice():
    print("Choose: (r)ock - (p)aper - (s)cissors")
    choice = input("Your choice [r/p/s]: ").strip().lower()
    while choice not in ["r", "p", "s"]:
        print("Invalid input, please enter r, p, or s.")
        choice = input("Your choice [r/p/s]: ").strip().lower()
    return choice


def get_computer_choice():
    return random.choice(["r", "p", "s"])


def convert_choice(short):
    return {"r": "rock", "p": "paper", "s": "scissors"}[short]


def determine_winner(user, computer):
    if user == computer:
        return "tie"
    elif (
        (user == "r" and computer == "s")
        or (user == "s" and computer == "p")
        or (user == "p" and computer == "r")
    ):
        return "user"
    else:
        return "computer"


def play_game():
    print("🎮 Welcome to Rock, Paper, Scissors (r/p/s)!")

    while True:
        try:
            rounds = int(input("How many rounds do you want to play? "))
            if rounds <= 0:
                print("Please enter a positive number.")
                continue
            break
        except ValueError:
            print("Invalid input. Please enter a number.")

    user_score = 0
    computer_score = 0
    ties = 0

    for i in range(1, rounds + 1):
        print(f"\n--- Round {i} ---")
        user_choice = get_user_choice()
        computer_choice = get_computer_choice()

        print(f"You chose: {convert_choice(user_choice)}")
        print(f"Computer chose: {convert_choice(computer_choice)}")

        result = determine_winner(user_choice, computer_choice)
        if result == "user":
            print("You win this round! 🎉")
            user_score += 1
        elif result == "computer":
            print("Computer wins this round! 💻")
            computer_score += 1
        else:
            print("It's a tie!")
            ties += 1

    print("\n🎯 Game Over!")
    print(f"Your score: {user_score}")
    print(f"Computer score: {computer_score}")
    print(f"Ties: {ties}")


# Start the game
play_game()
