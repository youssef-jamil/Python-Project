import random

#! Create the game to get from the user input as a char
# ? What is the game about?
# * The game is about two players who take turns to play a game of Rock, Paper, Scissors.
# * Each player chooses one of the three options: Rock, Paper, or Scissors.
# * The winner is determined by the rules of the game: Rock beats Scissors, Scissors beats Paper, and Paper beats Rock.
# * If both players choose the same option, the game is a tie.
# * The goal of the game is to win the most rounds by correctly choosing the option that beats the opponent's choice.

# ? What is the purpose of the game?
# ? What are the rules of the game?
# * The inputs are the choices of the two players: Rock, Paper, or Scissors.
# * The outputs are the results of each round: win, lose, or tie.
# * The game continues until one player wins a predetermined number of rounds (e.g., 3 rounds).
# ? What are the inputs and outputs of the game?
# * the output the winner of the game and the score of the game.


def output_results():
    list_of_choices = ["r", "p", "s"]
    scorePlayer1 = 0
    scorePlayer2 = 0
    n = int(input("Enter the number of rounds: "))
    # yousef
    for counter in range(1, n + 1):
        choos_player1 = input(
            "You, enter your choice (r for Rock, p for Paper, s for Scissors): "
        ).lower()
        choos_player2 = random.choice(list_of_choices)
        choice = choos_player1
        while choice not in list_of_choices:
            print("Invalid input, please enter r, p, or s.")
            choice = input(
                "You, enter your choice (r for Rock, p for Paper, s for Scissors): "
            ).lower()
        if choos_player1 == choos_player2:
            print(
                f"the round {counter} is a tie. Because both players choose {choos_player1}."
            )
        elif (
            (choos_player1 == "r" and choos_player2 == "s")
            or (choos_player1 == "s" and choos_player2 == "p")
            or (choos_player1 == "p" and choos_player2 == "r")
        ):

            print(
                f"the round {counter} is a win for You. Because You chose {choos_player1} and Computer chose {choos_player2}."
            )
            scorePlayer1 += 1  # test the git push
        else:
            print(
                f"the round {counter} is a win for Computer. Because You chose {choos_player1} and Computer chose {choos_player2}."
            )

            scorePlayer2 += 1
        counter += 1

    if scorePlayer1 > scorePlayer2:
        playerWin = "Player 1"
    elif scorePlayer1 < scorePlayer2:
        playerWin = "Player 2"
    else:
        playerWin = "No one"

    return scorePlayer1, scorePlayer2, playerWin, n - (scorePlayer1 + scorePlayer2)


list_of_choices = ["r", "p", "s"]

list_output = output_results()

if list_output[2] == "Player 1":
    print("========================================================")
    print("🎯 Game Over!")
    print(
        f"You win the game with {list_output[0]} rounds won.and the score of the game is {list_output[0]}:{list_output[1]} for You.and tie in {list_output[3]} rounds."
    )
elif list_output[2] == "Player 2":
    print("========================================================")
    print("🎯 Game Over!")
    print(
        f"Computer is wins the game with {list_output[1]} rounds won.and the score of the game is {list_output[0]}:{list_output[1]} for the Computer.and tie in {list_output[3]} rounds."
    )
else:
    print("========================================================")
    print("🎯 Game Over!")

    print(
        f"the game is a tie with the score of {list_output[0]}:{list_output[1]} for both players.and in this game there is no winner and tie in {list_output[3]} rounds."
    )
