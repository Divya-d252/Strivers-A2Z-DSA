# https://practice.geeksforgeeks.org/problems/reverse-bits3556/1
  
class Solution:
    def reversedBits(self, X):
        s=bin(X)[2:]
        s= ((32-len(s))*"0"+s)[::-1]
        return int(s,2)
      
import math
class Solution:
    def reversedBits(self, X):
        s = ""
        while(X>0):
            a=X%2
            s+=str(a)
            X=X//2
        s = int(s+(32-len(s))*"0")
        i = 0
        n = 0
        while(s>0):
            a=s%10
            n+=int(a*math.pow(2,i))
            s=s//10
            i+=1
        return n
      
# https://leetcode.com/problems/reverse-integer/submissions/
      
class Solution:
    def reverse(self, x: int) -> int:
        if x > 0:
            ans = int(str(x)[::-1])
        else:
            ans = int(str(x * -1)[::-1]) * -1
        
        mi = 2 ** 31 * (-1)
        ma = 2 ** 31 - 1
        
        if ans > ma or ans < mi:
            return 0
        return ans
