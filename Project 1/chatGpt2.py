import random  # ?  Import the random module for generating the computer's choices

# * Rock, Paper, Scissors Game
# * This program allows the user to play Rock, Paper, Scissors against the computer.
# * The user enters how many rounds they want to play.
# * In each round, the user chooses 'r' for rock, 'p' for paper, or 's' for scissors.
# * The computer randomly chooses a move.
# * The winner is decided based on the classic game rules.
# * At the end, the program shows the total number of wins, losses, and ties.


# Function to get the user's choice
def get_user_choice():
    print("Choose: (r)ock - (p)aper - (s)cissors")
    choice = input("Your choice [r/p/s]: ").strip().lower()

    # Validate input
    while choice not in ["r", "p", "s"]:
        print("Invalid input, please enter r, p, or s.")
        choice = input("Your choice [r/p/s]: ").strip().lower()

    return choice


# Function to get a random choice for the computer
def get_computer_choice():
    return random.choice(["r", "p", "s"])


# Function to convert the short choice to full name for display
def convert_choice(short):
    return {"r": "rock", "p": "paper", "s": "scissors"}[short]


# Function to determine the winner of a round
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


# Main function to run the game
def play_game():
    print("🎮 Welcome to Rock, Paper, Scissors (r/p/s)!")

    # Ask how many rounds the player wants to play
    while True:
        try:
            rounds = int(input("How many rounds do you want to play? "))
            if rounds <= 0:
                print("Please enter a positive number.")
                continue
            break
        except ValueError:
            print("Invalid input. Please enter a number.")

    # Initialize scores
    user_score = 0
    computer_score = 0
    ties = 0

    # Play the specified number of rounds
    for i in range(1, rounds + 1):
        print(f"\n--- Round {i} ---")
        user_choice = get_user_choice()
        computer_choice = get_computer_choice()

        print(f"You chose: {convert_choice(user_choice)}")
        print(f"Computer chose: {convert_choice(computer_choice)}")

        # Determine winner and update scores
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

    # Display final scores
    print("\n🎯 Game Over!")
    print(f"Your score: {user_score}")
    print(f"Computer score: {computer_score}")
    print(f"Ties: {ties}")
    if user_score > computer_score:
        print("Congratulations! You are the overall winner! 🏆")
    elif user_score < computer_score:
        print("Computer is the overall winner! Better luck next time! 🤖")
    else:
        print("It's an overall tie! 🤝")


# Start the game
play_game()
