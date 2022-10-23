# Input: 5

# Output:

#     *
#    ***  
#   *****
#  *******
# *********

class Solution:
    def printTriangle(self, N):
        for i in range(0,N):
            for j in range(0,N+i):
                if (i+j)>=N-1:
                    print("*",end="")
                else:
                    print(" ",end="")
            print()
