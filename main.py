import random

while True:

    choices = ["rock","paper","scissors"]
    computer = random.choice(choices)
    player = None # null variable so that it can be use

    while player not in choices:
        player = input("rock,paper, or scissors?: ").lower()

    if player == computer:
        print("computer: ", computer)
        print("player: ", player)
        print("Tie")

    elif player == "rock": #rock
        if computer == "paper":
            print("computer: ", computer)
            print("player: ", player)
            print("You lose")
        if computer == "scissors":
            print("computer: ", computer)
            print("player: ", player)
            print("You lose")

    elif player == "paper": #paper
        if computer == "rock":
            print("computer: ", computer)
            print("player: ", player)
            print("You win")
        if computer == "scissors":
            print("computer: ", computer)
            print("player: ", player)
            print("You lose")

    elif player == "scissors": #scissors
        if computer == "paper":
            print("computer: ", computer)
            print("player: ", player)
            print("You lose")
        if computer == "rock":
            print("computer: ", computer)
            print("player: ", player)
            print("You lose")
    play_again = input("Play again? (yes/no): ").lower()

    if play_again != "yes":
        break

print("Bye!")