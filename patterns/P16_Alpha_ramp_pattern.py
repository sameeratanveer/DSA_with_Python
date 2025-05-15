# Given an integer N, print the following pattern :
"""
Input Format: N = 3
Result: 
A
B B
C C C
"""

def alpha_ramp_bf(N):
    alpha = 65
    for i in range(1, N+1):
        # print(chr(alpha)*i)
        for j in range(i):
            print(chr(alpha), end=' ')
        print()
        alpha += 1

alpha_ramp_bf(6)