# Given an integer N, print the following pattern : 
"""
Input Format: N = 3
Result: 
******
**  **
*    *
*    *
**  **
******
"""

# Brute force:
def symmetric_void_pattern_bf(N):
    for i in range(N):
        for j in range(N-i):
            print('*', end='')
        for j in range(2*i):
            print(' ', end='')
        for j in range(N-i):
            print('*', end='')
        print()
    for i in range(N-1,-1,-1):
        for j in range(N-i):
            print('*', end='')
        for j in range(2*i):
            print(' ', end='')
        for j in range(N-i):
            print('*', end='')
        print()
# Pythonic version:
def symmetric_void_pattern_pv(N):
    for i in range(N):
        print('*'*(N-i), end='')
        print(' '*(2*i), end='')
        print('*'*(N-i), end='')
        print()
    for i in range(N-1,-1,-1):
        print('*'*(N-i), end='')
        print(' '*(2*i), end='')
        print('*'*(N-i), end='')
        print()
symmetric_void_pattern_bf(5)
