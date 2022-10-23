# Input: 5

# Output:
# A
# BB
# CCC
# DDDD
# EEEEE

class Solution:
    def printTriangle(self, N):
        # Code here
        c="ABCDEFGHIJKLMNOPQRSTUVWXYZ"
        for i in range(N):
            for j in range(i+1):
                print(c[i],end="")
            print()
