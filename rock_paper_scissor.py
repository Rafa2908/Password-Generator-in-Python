import random

win = 0
lose = 0

while True:
    print("------------- Rock Paper Scissors Game -------------")
    computer = random.randint(1, 3)

    if computer == 1:
        computer = "rock"
    elif computer == 2:
        computer = "paper"
    else:
        computer = "scissor"

    player = str(input("Enter your choice (rock, paper, scissor): ")).lower()
    if player == "rock" and computer == "rock":
        print("It's a draw. Play again")

    elif player == "paper" and computer == "rock":
        print("You won!!")
        win += 1

    elif player == "scissor" and computer == "rock":
        print("You lost")
        lose += 1

    elif player == "paper" and computer == "paper":
        print("It's a draw. Play again")

    elif player == "scissor" and computer == "paper":
        print("You won!!")
        win += 1

    elif player == "rock" and computer == "paper":
        print("You lost")
        lose += 1

    elif player == "scissor" and computer == "scissor":
        print("It's a draw. Play again")

    elif player == "paper" and computer == "scissor":
        print("You lost")
        lose += 1
    else:
        print("You won!!")
        win += 1

    print(f"Player's Move: {player.upper()} - Computer's Move: {computer.upper()}")
    print(f"Score:\n Win: {win} Lose: {lose}")

    play_again = str(input("Would you like to play again (y/n): "))
    if play_again.lower() == "n":
        print("----- Thank you for playing ----- ")
        break
print(f"Score:\n Win: {win} Lose: {lose}")
