#  Given an integer N, print the following pattern : 
"""
Input Format: N = 3
Result: 
A
A B
A B C
"""

def increasing_letter_triangle_bf(N):
    for i in range(65, 65+N):
        for j in range(65, i+1):
            print(chr(j), end='')
        print()


increasing_letter_triangle_bf(3)