# Given an integer N, print the following pattern : 
"""
Input Format: N = 6
Result:   
     *
     **
     *** 
     ****
     *****
     ******  
     *****
     ****
     ***    
     **
     *
"""

def half_diamond_star_bf(N):
    # top star.. 
    for i in range(1,N):
        for j in range(i):
            print('*', end='')
        print()
    # bottom star..
    for i in range(N, 0, -1):
        for j in range(i):
            print('*', end='')
        print()


# Pythonic version..
def half_diamond_star_pv(N):
    # top star
    for i in range(1, N):
        print('*'*i)
    # bottom star
    for i in range(N, 0, -1):
        print('*'*i)


half_diamond_star_bf(3)
print()
half_diamond_star_pv(3)