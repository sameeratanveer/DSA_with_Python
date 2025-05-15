# Given an integer N, print the following pattern : 
"""
Input Format: N = 3
Result: 
  A  
 ABA 
ABCBA
"""

def alpha_hill_bf(N):
    # alpha = 65
    for i in range(1, N+1):
        for j in range(i):
            alpha = 65
            # spaces
            print('-'*(N-j), end='')

            # char.. 
            for charac in range(j):
                print(chr(alpha), end='')
                alpha += 1
            
            # alpha = 65 + N
            # # char.. 
            # for charac in range(j+1):
            #     print(chr(alpha), end='')
            #     alpha -=1
            # # spaces..
            # # spaces
            # print('-'*(N-j), end='')
        print()



alpha_hill_bf(3)