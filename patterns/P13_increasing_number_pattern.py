# Given an integer N, print the following pattern : 
"""
Input Format: N = 3
Result: 
1
2 3
4 5 6
"""

def increasing_number_pattern_bf(N):
    numb = 1
    for i in range(N):
        for j in range(i+1):
            print(numb, end=' ')
            numb += 1
        print()

increasing_number_pattern_bf(3)