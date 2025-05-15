# Given an integer N, print the following pattern : 
"""
Input Format: N = 6
Result:
1 2 3 4 5 6
1 2 3 4 5
1 2 3 4
1 2 3
1 2 
1
"""

# Brute force:
def inverted_numbered_right_pyramid(N):
    for i in range(N, 0, -1):
        for j in range(1, i+1):
            print(j, end='')
        print()

# Pythonic version:
def inverted_numbered_right_pyramid_pv(N):
    for i in range(N, 0, -1):
        print(str(i)*(i))

inverted_numbered_right_pyramid_pv(6)

