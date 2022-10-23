# Input: 4
# Output:
#    A
#   ABA
#  ABCBA
# ABCDCBA

class Solution:
    def printTriangle(self, N):
        for i in range(N):
            k=0
            for j in range(2*N-1):
                if(i+j<N-1):
                    print(end=" ")
                elif(j<N):
                    k=k+1
                    print(chr(64+k),end="")
                elif(j<N+i):
                    k=k-1
                    print(chr(64+k),end="")
            print()
