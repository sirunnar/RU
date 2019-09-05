# Unnar Sigurðsson
# Design an algorithm that finds the maximum positive integer input by a user.  
# The user repeatedly inputs numbers until a negative value is entered.
 

num_int = int(input("Input a number: "))    # Do not change this line
# Fill in the missing code

num_int_max = 0
counter = 0

while counter < 0:
    if num_int < 0:
        break
    num_int = int(input("Input a number: ")) 
    if num_int_max < num_int:
        num_int_max = num_int
        


print("The maximum is", max_int)    # Do not change this line
