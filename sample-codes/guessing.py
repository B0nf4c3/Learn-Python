# A guessing game using loops and the random mudule
import random
ran_no = random.randint(1,10)

while True:
    gues = int(input("Enter your lucky no : "))
    if gues < 1 or gues > 10:
        print("Please enter a number between 1 and 10")
        continue
    if gues == ran_no:
        print("You won")
    elif gues < ran_no:
        print("Too low")
    else:
        print("Too High")
        play_again = input("Do you want to play again? (y/n)").lower()
        if play_again == "y":
            ran_no = random.randint(1,10)
        else:
            print("Thank you for playing")
            break
     
# future improvements :
# 1. Add a counter to count the number of guesses
# 2. validate the user input to ensure it is a number


