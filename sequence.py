# Unnar Sigurðsson

# Design an algorithm that generates the first n numbers 
# in the following sequence:; 1, 2, 3, 6, 11, 20, 37, ___, ___, ___, 

n = int(input("Enter the length of the sequence: ")) # Do not change this line
counter = 0

int_first = 1
int_third = 0
int_secont = 0
int_forth = 0

int_sum = 0

while counter < n:
    print(counter, end="")
    counter += 1

    int_sum = int_forth + int_third + int_secont + int_first

    int_forth = int_third
    int_third = int_secont
    int_secont = int_first
    int_first = int_sum

    print(int_sum)

