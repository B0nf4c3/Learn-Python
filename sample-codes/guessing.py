# A guessing game using loops and the random mudule
import random
ran_no = random.randint(1,10)

while True:
    gues = int(input("Enter your lucky no"))
    if gues == ran_no:
        print("You won")
    elif gues < ran_no:
        print("Too low")
    else:
        print("Too low")

