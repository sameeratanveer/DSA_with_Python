# Given an integer N, print the following pattern : 
"""
Input Format: N = 6
Result:   
     *
    ***
   ***** 
  *******
 *********
***********  
***********
 *********
  *******
   ***** 
    ***    
     *
"""
def top_star(N):
    for i in range(N):
        for space in range(N-i-1):
            print(' ', end='')
        for star in range(2*i+1):
            print('*', end='')
        for space in range(N-i-1):
            print(' ', end='')
        print()

def bottom_star(N):
    for i in range(N-1, -1, -1):
        for space in range(N-i-1):
            print(' ', end='')
        for star in range(2*i+1):
            print('*', end='')
        for space in range(N-i-1):
            print(' ', end='')
        print()

def diamond_star_pattern_bf(N):
    top_star(N)
    bottom_star(N)

def diamond_star_pattern_pv(N):
    # top face of diamong
    for i in range(N):
        print(' '*(N-i-1), end='')
        print('*'*(2*i+1), end='')
        print(' '*(N-i-1), end='')
        print()
    
    # bottom face of diamond
    for i in range(N-1, -1, -1):
        print(' '*(N-i-1), end='')
        print('*'*(2*i+1), end='')
        print(' '*(N-i-1), end='')
        print()

diamond_star_pattern_bf(6)
print()
diamond_star_pattern_bf(6)