# Given an integer N, print the following pattern : 
"""
Input Format: N = 5
Result:
* 
* * 
* * *
* * * *
* * * * *

from the above pattern, we can say that:
cols = current th Row
"""

# Brute force:
def right_angle_triangle_bf(N):
    for i in range(N): # Handles Rows
        for j in range(i+1): # Handles cols = current th Row
            print("*", end='') # prints * a row
        print() # next row..

# Pythonic version
def right_angle_triangle_pv(N):
    for i in range(N):
        print("*"*(i+1))

right_angle_triangle_bf(5)
right_angle_triangle_pv(5)

"""
Which one is best in performance?
Again Pv.. because of the string multiplication.. it's time complexity is O(N)
while bf time complexity is O(N2)"""
