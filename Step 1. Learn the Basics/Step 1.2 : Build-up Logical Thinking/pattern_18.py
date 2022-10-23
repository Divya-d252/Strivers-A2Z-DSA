# Input: 5

# Output:
# E
# E D
# E D C
# E D C B
# E D C B A

class Solution:
    def printTriangle(self, N):
        for i in range(N):
            for j in range(i+1):
                print(chr(N-j+64),end=" ")
            print()
            
# E
# D E
# C D E
# B C D E
# A B C D E

class Solution:
    def printTriangle(self, N):
        for i in range(N):
            for j in range(i,-1,-1):
                print(chr(N-j+64),end=" ")
            print()
