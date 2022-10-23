# For Input: 
# 6

# Your Output: 
#      *
#     * *
#    * * *
#   * * * *
#  * * * * *
# * * * * * *
# * * * * * *
#  * * * * *
#   * * * *
#    * * *
#     * *
#      *
      
class Solution:
    def printTriangle(self, N):
        for i in range(0,N):
            for j in range(0,N+i+1):
                if (i+j)>=N-1 and ((N%2==1 and (i+j)%2==0) or (N%2==0 and (i+j)%2==1)):
                    print("*",end="")
                else:
                    print(" ",end="")
            print()
        for i in range(N-1,-1,-1):
            for j in range(N+i+1):
                if(i+j >= N-1) and ((N%2==1 and (i+j)%2==0) or (N%2==0 and (i+j)%2==1)):
                    print("*",end="")
                else:
                    print(" ",end="")
            print()
