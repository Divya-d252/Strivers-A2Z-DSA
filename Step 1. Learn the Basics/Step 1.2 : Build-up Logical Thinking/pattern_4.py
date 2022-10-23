# Input: 5

# Output:
# 1
# 2 2 
# 3 3 3 
# 4 4 4 4 
# 5 5 5 5 5

class Solution:
    def printTriangle(self, N):
        for i in range(N):
            for j in range(N):
                if(i>=j):
                    print(i+1,end=" ")
            print()
