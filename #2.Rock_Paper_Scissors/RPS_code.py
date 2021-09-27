from random import randint 
choice = ["rock", "paper", "scissors"]
while True:
    option = input("Want to play (y/n): ")
    if "n" in option.lower():
        break
    if "y" in option.lower():
        player = str(input("You choose Rock, Paper, Scissors: "))
        if player.lower() in choice:
            computer = randint(0,2)
            if computer == 0: computer = "rock"
            if computer == 1: computer = "paper"
            if computer == 2: computer = "scissors"
            print("----------")
            print("You choose: " + player.lower().capitalize())
            print("Computer choose: " + computer.capitalize())
            print("----------")
            if player.lower() == computer:
                print("Draw")
            if player.lower() == "rock":
                if computer == "scissors":
                    print("You Win")
                elif computer == "paper":
                    print("You Lose")
            if player.lower() == "paper":
                if computer == "rock":
                    print("You Win")
                elif computer == "scissors":
                    print("You Lose")
            if player.lower() == "scissors":
                if computer == "paper":
                    print("You Win")
                elif computer == "rock":
                    print("You Lose")
        else:
            continue
print("END")
