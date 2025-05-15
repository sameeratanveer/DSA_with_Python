# Given an integer N, print the following pattern : 
"""
Input Format: N = 6
Result:   
******
*    *
*    *
*    *
*    *
******
"""

def hollow_rectangle_pv(N):
    for i in range(1, N+1):
        if i == 1 or i == N:
            print('*'*N)
        else:
            print('*', end='')
            print(' '*(N-2), end='')
            print('*', end='')
            print()

hollow_rectangle_pv(6)