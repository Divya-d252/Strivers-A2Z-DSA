# Count Digits in a number

# Example 1:
# Input: N = 12345
# Output: 5
# Explanation: N has 5 digits

# 1. Convert to string -> s = str(N) -> len(s) 
# 2. Counting No of digits

while(N>0):
    N=N//10
    c+=1
return c

# 3. Best Approach - O(1) time complexity

import math
class Solution:
    def countDigits(self, N):
        return math.ceil(math.log10(N))
  
# https://practice.geeksforgeeks.org/problems/count-digits5716/1
  
class Solution:
    def evenlyDivides (self, N):
        c=0
        temp = N
        while(temp>0):
            a=temp%10
            if(a!=0 and N%a==0):
                c+=1
            temp=temp//10
        return c
