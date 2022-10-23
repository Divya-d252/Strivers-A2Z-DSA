# Input: 5

# Output:
# * 
# * * 
# * * * 
# * * * * 
# * * * * *
# * * * *
# * * *
# * *
# *

class Solution:
    def printTriangle(self, N):
        # Code here
        for i in range(N-1):
            for j in range(i+1):
                print("* ", end='')
            print()
        for i in range(N):
            for j in range(i, N):
                print("* ", end="")
            print()
