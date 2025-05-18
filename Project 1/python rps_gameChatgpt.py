import random


def get_user_choice():
    print("Choose: (r)ock - (p)aper - (s)cissors")
    choice = input("Your choice [r/p/s]: ").strip().lower()
    while choice not in ["r", "p", "s"]:
        print("Invalid input, please enter r, p, or s.")
        choice = input("Your choice [r/p/s]: ").strip().lower()
    return choice


# بببببببب
def get_computer_choice():
    return random.choice(["r", "p", "s"])


def convert_choice(short):
    return {"r": "rock", "p": "paper", "s": "scissors"}[short]


def determine_winner(user, computer):
    if user == computer:
        return "It's a tie!"
    elif (
        (user == "r" and computer == "s")
        or (user == "s" and computer == "p")
        or (user == "p" and computer == "r")
    ):
        return "You win! 🎉"
    else:
        return "Computer wins! 💻"


def play_game():
    print("🎮 Welcome to Rock, Paper, Scissors (r/p/s)!")
    user_choice = get_user_choice()
    computer_choice = get_computer_choice()

    print(f"\nYou chose: {convert_choice(user_choice)}")
    print(f"Computer chose: {convert_choice(computer_choice)}")
    print(determine_winner(user_choice, computer_choice))


# Start the game
play_game()
