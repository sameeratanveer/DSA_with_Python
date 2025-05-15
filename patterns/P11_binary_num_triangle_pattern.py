# Given an integer N, print the following pattern : 
"""
Input Format: N = 3
Result: 
1
01
101

"""

def binary_num_triangle_bf(N):
    for i in range(1, N+1):
        curr = i%2
        for j in range(i):
            print(curr, end='')
            curr = 0 if curr == 1 else 1
            # if curr == 1:
            #     curr = 0
            # else:
            #     curr = 1
        print()

binary_num_triangle_bf(3)
