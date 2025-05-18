import random

min_attempts = float("inf")

while True:
    print("\nWelcome to the guessing game!")
    print("I'm thinking of a number between 1 and 10.")

    try:
        player_choice = int(input("Your guess: "))
    except ValueError:
        print("Please enter a valid number.")
        continue

    pc_choice = random.randint(1, 10)
    attempts = 1

    while player_choice != pc_choice:
        if player_choice < pc_choice:
            print("Too low, try again.")
        else:
            print("Too high, try again.")
        try:
            player_choice = int(input("Your guess: "))
        except ValueError:
            print("Please enter a valid number.")
            continue
        attempts += 1

    if attempts < min_attempts:
        min_attempts = attempts

    print(f"🎉 Congratulations! You guessed the number in {attempts} attempt(s).")
    print(f"⭐ Minimum number of attempts so far: {min_attempts}")

    play_again = input("Do you want to play again? (yes/no): ")
    if play_again.strip().lower() != "yes":
        print("Thanks for playing! Goodbye!")
        break
