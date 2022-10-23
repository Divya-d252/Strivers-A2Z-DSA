# Input: 5

# Output:
# ABCDE
# ABCD
# ABC
# AB
# A

class Solution:
    def printTriangle(self, N):
        c="ABCDEFGHIJKLMNOPQRSTUVWXYZ"
        for i in range(N):
            for j in range(N):
                if(i+j<N):
                    print(c[j],end="")
            print()
