# Given an integer N, print the following pattern : 
"""
Input Format: N = 5
Result:
     *     
    ***    
   *****   
  *******  
 ********* 

spaces are even on both the sides of the *
Number of spaces we can get after checking is int(2N-1/2)
number of *'s => 2i+1
"""
# Brute force approach:
def star_pyramid_bf(N):
    for i in range(N):
        for space in range(N-i-1):
            print(' ', end='')
        for star in range(2*i+1):
            print('*', end='')
        for space in range(N-i-1):
            print(' ', end='')
        print()


# Pythonic version:
def star_pyramid_pv(N):
    for i in range(N):
        print(' '*(N-i-1), end='')
        print('*'*(2*i+1), end='')
        print(' '*(N-i-1), end='')
        print()


star_pyramid_bf(5)
star_pyramid_pv(5)