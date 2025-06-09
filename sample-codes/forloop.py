# for loop
# Task
# Loop through numbers 1-20
# - for 4 and 13 ,ptint "X is unlucky"
# - for even numbers, print " X is even"
# - for odd numbers, print " X is odd"

for x in range(1,21):
    if x == 4 or x == 13:
        print(f"{x} is unlucky")
    elif x % 2 == 0:
        print(f"{x} is even")
    else:
        print(f"{x} is odd")
