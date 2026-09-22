# In this i will try to create a simple rock paper scissors game
# While this is a simple version, it can be expanded with more features later.
# Will be using the knowledge of : variables, conditions, input and print functions.

print("Welcome to my simple Rock Paper Scissors game!")
print("You will be playing against the computet.")
print("Good Luck! \nLet the game begin!")
print("*" * 20)

print("Player 1")
player1 = input("Choose from :\n---> Rock \n---> Paper \n---> Scissors\n\n--->").lower()
if player1 and player1 in ["rock", "paper", "scissors"]:
    print(f"Nice Player one chooses {player1}")
else:
    print("Invalid choice. Please choose Rock, Paper, or Scissors.")
    exit()


print("\n\n\nPlayer 2")
player2 = input("Choose from :\n---> Rock \n---> Paper \n---> Scissors\n\n--->").lower()
if player2 and player2 in ["rock", "paper", "scissors"]:
    print(f"Nice Player two chooses {player2}")
else:
    print("Invalid choice. Please choose Rock, Paper, or Scissors.")
    exit()


print("\n\n" + "*" * 20 +"\n\n")
if player1 == player2:
    print("It's a tie!")
elif (player1 == "rock" and player2 == "scissors") or \
	 (player1 == "paper" and player2 == "rock") or \
	 (player1 == "scissors" and player2 == "paper"):
    print("Player 1 wins!")
else:
	print("Player 2 wins!")

print(f"since : player one had {player1} and player two had {player2}")
print("Thanks for playing!")