# Given an integer N, print the following pattern : 
"""
Input Format: N = 6
Result:     
***********
 *********
  *******
   ***** 
    ***    
     *
"""
def inverted_star_pyramid_bf(N):
    for i in range(N-1, -1, -1):
        for space in range(N-i-1):
            print(' ', end='')
        for star in range(2*i+1):
            print('*', end='')
        for space in range(N-i-1):
            print(' ', end='')
        print()

#Pythonic version:
def inverted_star_pyramid_pv(N):
    for i in range(N-1, -1, -1):
        print(' '*(N-i-1), end='')
        print('*'*(2*i+1), end='')
        print(' '*(N-i-1), end='')
        print()

inverted_star_pyramid_pv(5)