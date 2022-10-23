# Input: 5

# Output:
# 1
# 1 2 
# 1 2 3 
# 1 2 3 4 
# 1 2 3 4 5

class Solution:
    def printTriangle(self, N):
        for i in range(N):
            for j in range(N):
                if(i>=j):
                    print(j+1,end=" ")
            print()
