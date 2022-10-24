# Solution 1: Brute force
  
# Time Complexity: O(N).
# Space Complexity: O(1).
  
class Solution:
    def lcmAndGcd(self, A , B):
        for i in range(1,min(A,B)+1):
            if(A%i==0 and B%i==0):
                gcd=i
        return (A*B)//gcd,gcd
      
# Solution 2: Using Euclidean’s theorem.
# Intuition: Gcd is the greatest number which is divided by both a and b.If a number is divided by both a and b, it is should be divided by (a-b) and b as well.
  
# GCD(A,B) = GCD(B,A%B)

# Approach:
# 1. Recursively call gcd(b,a%b) function till the base condition is hit.
# 2. b==0 is the base condition.When base condition is hit return a,as gcd(a,0) is equal to a.
      
# Time Complexity: O(logɸmin(a,b)),where ɸ is 1.61.
# Space Complexity: O(1).
      
class Solution:
    def GCD(self,A,B):
        if(B==0):
            return A
        else:
            return Solution.GCD(self,B,A%B)
    def lcmAndGcd(self, A , B):
        gcd = Solution.GCD(self,A,B)
        return (A*B)//gcd,gcd
