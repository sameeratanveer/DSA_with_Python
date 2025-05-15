# Given an integer N, print the following pattern : 
"""
Input Format: N = 6
Result:
* * * * * *
* * * * * 
* * * * 
* * * 
* * 
* 
"""

# Brute force:
def inverted_right_angle_bf(N):
    for i in range(N, 0, -1):
        for j in range(i):
            print('*', end='')
        print()

# Pythonic version
def inverted_right_angle_pv(N):
    for i in range(N, 0, -1):
        print("*"*i)

inverted_right_angle_pv(6)