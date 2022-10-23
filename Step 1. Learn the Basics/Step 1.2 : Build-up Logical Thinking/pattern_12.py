# Input: 5

# Output:
# 1                 1
# 1 2             2 1
# 1 2 3         3 2 1
# 1 2 3 4     4 3 2 1
# 1 2 3 4 5 5 4 3 2 1

class Solution:
    def printTriangle(self, N):
        for i in range(N):
            for j in range(2*N):
                if(i>=j or i+j>=(2*N)-1):
                    print(min(j+1,(2*N)-j),end=" ")
                else:
                    print(" ",end=" ")
            print()
