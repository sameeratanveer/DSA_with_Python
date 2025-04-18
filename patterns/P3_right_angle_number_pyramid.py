# Given an integer N, print the following pattern : 
"""
Input Format: N = 5
Result:
1
1 2
1 2 3
1 2 3 4
1 2 3 4 5

SAME as before except * is replaced by number == col
"""

# brute force
def right_angled_number_pyramid_bf(N):
    for i in range(N): # Handles Row
        for j in range(i+1): # Handles Cols
            print(j+1, end='') # prints j+1 because range index starts from 0, but pattern cols starts from 1
        print() # New line

# PV
def right_angled_number_pyramid_pv(N):
    for i in range(N):
        print(''.join(str(x) for x in range(1, i+1))) 
        # what's happening?
        # so,  numbers from 1 to current row.. and convert it to string from object.. and join in for every number from the range..
        # the only benefit of this is reducing printing operations.. i/o opeeration overhead is reduced..

right_angled_number_pyramid_bf(5)
right_angled_number_pyramid_pv(5)

"""
Brtute force Complexity= O(N2)
pythonic version = O(N2) but efficient in i/o operations
because in brute force the printing is done N2 + N times 
but in pv : its only N times..

"""
