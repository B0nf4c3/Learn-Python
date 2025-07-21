# In this i will try to improve our simple rock paper scissors game
# Will be adding on the concept of loops and rondom module 

import random
tie = 0
player = 0
comp = 0

print("Welcome to my simple Rock Paper Scissors game!")
print("You will be playing against the computet.")
print("Let's do a best of 3 game. The first to win 2 rounds wins the game.")
print("Good Luck! \nLet the game begin!")
print("*" * 20 + "\n\n")

for count in range(3):
    print(f"Round {count + 1} of 3")
    print("Player 1")
    player1 = input("Choose from :\n---> Rock \n---> Paper \n---> Scissors\n\n--->").lower()
    if player1 and player1 in ["rock", "paper", "scissors"]:
        print("\n\n" + "*" * 20 + "\n\n")
        print(f"Nice Player one chooses {player1}")
    else:
        print("Invalid choice. Please choose Rock, Paper, or Scissors.")
        exit()


    rand_no = random.randint(1,4)
    if rand_no == 1:
        computer = "rock"
    elif rand_no == 2:
        computer = "paper"
    else:
        computer = "scissors"

    if computer and computer in ["rock", "paper", "scissors"]:
        print(f"Nice computer chooses {computer}")
    else:
        print("Invalid choice. Please choose Rock, Paper, or Scissors.")
        exit()


    print("\n\n" + "*" * 20 +"\n\n")
    if player1 == computer:
        print("It's a tie! \n\n")
        tie += 1
    elif (player1 == "rock" and computer == "scissors") or \
        (player1 == "paper" and computer == "rock") or \
        (player1 == "scissors" and computer == "paper"):
        print("Player 1 wins! \n\n")
        player += 1
    else:
        print("computer wins! \n\n")
        comp += 1

print("Here are your results")
print(f"        - Player wins = {player}")
print(f"        - Computer Wins = {comp}")
print(f"        - Ties = {tie}")

if player == comp:
    print("It was a tie")
elif player > comp:
    print("You won")
else:
    print("Computer Wins and you loss")

print("Thanks for playing!")
