# Input: 5

# Output:
# A
# AB
# ABC
# ABCD
# ABCDE

class Solution:
    def printTriangle(self, N):
        c="ABCDEFGHIJKLMNOPQRSTUVWXYZ"
        for i in range(N):
            for j in range(i+1):
                print(c[j],end="")
            print()
