# Using while loops 
# Task
# Print the following art strings using booth a for loop and a while loop.
# 

print("*" * 20)
print("This is using the for loop")
for x in range(11):
    print("\U0001f600" * x)

print("\n\n" + "*" * 20 )
print("This is using the while loop")
count = 1
while count <=10:
    print("\U0001f600" * count ) 
    count += 1
