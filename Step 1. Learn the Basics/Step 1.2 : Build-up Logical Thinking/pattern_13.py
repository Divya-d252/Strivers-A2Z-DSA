# Input: 5

# Output:
# 1 
# 2 3 
# 4 5 6 
# 7 8 9 10 
# 11 12 13 14 15

class Solution:
    def printTriangle(self, N):
        k=1
        for i in range(N):
            for j in range(i+1):
                print(k,end=" ")
                k+=1
            print()
