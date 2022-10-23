# For Input: 
# 5
# Your Output: 
# *        *
# **      **
# ***    ***
# ****  ****
# **********
# ****  ****
# ***    ***
# **      **
# *        *

class Solution:
    def printTriangle(self, N):
        for i in range(N):
            for j in range(2*N):
                if(i>=j or i+j>=(2*N-1)):
                    print("*",end="")
                else:
                    print(" ",end="")
            print()
        for i in range(1,N):
            for j in range(2*N):
                if(i+j<N):
                    print("*",end="")
                elif(j>=N-1 and j-N-1>=i-1):
                    print("*",end="")
                else:
                    print(" ",end="")
            print()
