# Input: 5

# Output:

# *********
#  *******
#   *****
#    ***
#     *
    
class Solution:
    def printTriangle(self, N):
        for i in range(N-1,-1,-1):
            for j in range(N+i):
                if(i+j >= N-1):
                    print("*",end="")
                else:
                    print(" ",end="")
            print()
