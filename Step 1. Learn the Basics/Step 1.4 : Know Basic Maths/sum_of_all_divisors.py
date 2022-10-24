# Time Complexity: O(N**2)
# Space Complexity: O(1), we are not using any extra space.
  
class Solution:
    def sumOfDivisors(self, N):
        s=0
        for i in range(1,N+1):
            for j in range(1,i+1):
                if(i%j==0):
                    s+=j
        return s

# Time Complexity: O(N*sqrt(N)), because everytime the loop runs only sqrt(N) times.
# Space Complexity: O(1), we are not using any extra space.
      
import math
class Solution:
    def sumOfDivisors(self, N):
        s=0
        for i in range(1,N+1):
            for j in range(1,int(math.sqrt(i))+1):
                if(i%j==0):
                    s+=j
                    if(j!=i//j):
                        s+=(i//j)
        return s
      
# Time Complexity: O(N)
# Space Complexity: O(1), we are not using any extra space.
   
# Briliant Solution:
  
import math
class Solution:
    def sumOfDivisors(self, N):
        s=0
        for i in range(1,N+1):
            s+=(N//i)*i
        return s
