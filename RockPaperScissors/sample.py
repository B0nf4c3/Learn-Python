print("Rock Paper Scissors Game")
print("*" * 20)
import random
def get_computer_choice():
	choices = ["rock", "paper", "scissors"]
	return random.choice(choices)
def get_user_choice():
	choices = ["rock", "paper", "scissors"]
	while True:
		user_choice = input("Enter your choice (rock, paper, scissors): ").lower()
		if user_choice in choices:
			return user_choice
		else:
			print("Invalid choice. Please try again.")
def determine_winner(user_choice, computer_choice):
	if user_choice == computer_choice:
		return "It's a tie!"
	elif (user_choice == "rock" and computer_choice == "scissors") or \
			(user_choice == "paper" and computer_choice == "rock") or \
			(user_choice == "scissors" and computer_choice == "paper"):
		return "You win!"
	else:
		return "Computer wins!"
def play_game():
	user_choice = get_user_choice()
	computer_choice = get_computer_choice()
	print(f"You chose: {user_choice}")
	print(f"Computer chose: {computer_choice}")
	result = determine_winner(user_choice, computer_choice)
	print(result)
if __name__ == "__main__":
	play_game()
	while input("Do you want to play again? (yes/no): ").lower() == "yes":
		play_game()
	print("Thanks for playing!")
# This code implements a simple Rock Paper Scissors game where the user plays against the computer.
# The user can input their choice, and the computer randomly selects its choice.
# The winner is determined based on the rules of the game.
# The game continues until the user decides to stop playing.
# The code is structured to allow for easy expansion or modification in the future.