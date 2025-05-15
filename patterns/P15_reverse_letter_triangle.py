# Given an integer N, print the following pattern :
"""
Input Format: N = 3
Result: 
A B C
A B
A
"""
def reverse_letter_triangle_bf(N):
    for i in range(65+N, 65, -1):
        for j in range(65, i):
            print(chr(j), end=' ')
        print()

reverse_letter_triangle_bf(6)
