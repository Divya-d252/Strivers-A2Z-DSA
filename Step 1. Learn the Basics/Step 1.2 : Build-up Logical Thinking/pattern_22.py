# Input: 4

# Output:
# 4 4 4 4 4 4 4
# 4 3 3 3 3 3 4
# 4 3 2 2 2 3 4
# 4 3 2 1 2 3 4
# 4 3 2 2 2 3 4
# 4 3 3 3 3 3 4
# 4 4 4 4 4 4 4

class Solution:
    def printTriangle(self, N):
        for i in range(2*N-1):
            for j in range(2*N-1):
                print(N-min(min(i,2*N-2-i),min(j,2*N-2-j)),end=" ")
            print()
