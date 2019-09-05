# Unnar Sigurðsson

# Design an algorithm that generates the first n numbers 
# in the following sequence:; 1, 2, 3, 6, 11, 20, 37, ___, ___, ___, 

n = int(input("Enter the length of the sequence: ")) # Do not change this line
counter = 0


while counter < n:
    print(counter, end="")
    counter += 1
    
