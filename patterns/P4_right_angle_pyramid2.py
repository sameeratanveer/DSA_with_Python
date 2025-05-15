# Given an integer N, print the following pattern : 
"""
Input Format: N = 6
Result:
1
2 2
3 3 3
4 4 4 4
5 5 5 5 5
6 6 6 6 6 6
"""

# Brute force:
def right_angle_pyramid2_bf(N):
    for i in range(N):
        for j in range(i+1):
            print(i+1, end='')
        print()

# Pythonic version:
def right_angle_pyramid2_pv(N):
    for i in range(N):
        print(str(i+1)*(i+1))
right_angle_pyramid2_pv(6)