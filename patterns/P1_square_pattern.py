# Given an int 'N' print the following pattern
"""
*****
*****
*****
*****
*****

if N=5

from the above pattern we can see that N is same for both Rows and Cols.. making 
it a  perfect square..
"""

# Logic wise:
def print_pattern(N):
    for i in range(N): # Rows
        for j in range(N): # cols
            print("*", end="")
        print()
    return 0

print_pattern(5)

# Pythonic version
def print_pattern_pythonic(N):
    for i in range(N):
        print("*"*N) # Prints N times * completing the row..
    return 0

print_pattern_pythonic(6)

"""
Which one is best in performance?
My answer: 
As the first Logic wise have 2 loops making it O(N2)
wheread, the pythonic version is having 1 loop making it O(N) and 
string multiplication takes constant time

Hence Pythonic version is correct.."""


