# Given an integer N, print the following pattern : 
"""
Input Format: N = 3
Result: 
*    *
**  **
******
**  **
*    *
"""

def symmetric_butterfly_pv(N):
    spaces = 2*N-2 
    for i in range(N): 
        print('*'*(i+1), end='')  
        print(' '*spaces, end='')  
        print('*'*(i+1), end='')
        print()
        spaces -= 2
    spaces = 2
    for i in range(N-1, 0, -1):
        print('*'*(i), end='')
        print(' '*spaces, end='')
        print('*'*(i), end='')
        print()
        spaces += 2
        

symmetric_butterfly_pv(5)