# Given an integer N, print the following pattern : 
"""
Input Format: N = 3
Result: 
1    1
12  21
123321

"""
def number_crown_pattern_bf(N):
    for i in range(1,N+1):
        # Numbers
        for j in range(1,i+1):
            print(j, end='')
        # space 1
        for space in range(N-i):
            print(' ', end='')
        # space 2
        for space in range(N-i):
            print(' ', end='')
        # inverted numbers
        for j in range(i, 0, -1):
            print(j, end='')
        print()

# Pythonic version:
def number_crown_pattern_pv(N):
    for i in range(1, N+1):
        # numbers
        for j in range(1,i+1):
            print(j, end='')
        # spaces 
        print(' '*(2*(N-i)), end='')
        # inverted numbers
        for j in range(i, 0, -1):
            print(j, end='')
        print()

number_crown_pattern_bf(3)
print()
number_crown_pattern_pv(3)

