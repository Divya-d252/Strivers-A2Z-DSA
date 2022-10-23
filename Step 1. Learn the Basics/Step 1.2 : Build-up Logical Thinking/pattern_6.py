# Input: 5

# Output:
# 1 2 3 4 5
# 1 2 3 4
# 1 2 3 
# 1 2  
# 1 

class Solution:
    def printTriangle(self, N):
        for i in range(N):
            for j in range(N):
                if(i+j<N):
                    print(j+1,end=" ")
            print()
