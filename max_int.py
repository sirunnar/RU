# Unnar Sigurðsson
# Design an algorithm that finds the maximum positive integer input by a user.  
# The user repeatedly inputs numbers until a negative value is entered.
 

num_int = int(input("Input a number: "))    # Do not change this line
# Fill in the missing code

max_int = 0
counter = 0

while True:
    if num_int < 0:
        break
    num_int = int(input("Input a number: ")) 
    if max_int < num_int:
        max_int = num_int



print("The maximum is", max_int)    # Do not change this line
