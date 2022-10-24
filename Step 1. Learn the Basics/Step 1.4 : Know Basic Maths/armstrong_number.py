# What are Armstrong Numbers?
# Armstrong Numbers are the numbers having the sum of digits raised to power no. of digits is equal to a given number. 

# 1**4 + 6**4 + 3**4 + 4**4 = 1634

# Time Complexity: O(n) where n is the number of digits since we need to traverse every digit and add digits raised to power no. of digits to sum.
# Space Complexity: O(1) since no extra space is required
  
class Solution:
    def armstrongNumber (ob, n):
        temp=n
        s=0
        while(n>0):
            a=n%10
            s+=(a*a*a)
            n=n//10
        if(s==temp):
            return "Yes"
        else:
            return "No"
          
class Solution:
    def armstrongNumber (ob, n):
        l=len(str(n))
        temp=n
        s=0
        while(n>0):
            a=n%10
            s+=(a**l)
            n=n//10
        if(s==temp):
            return "Yes"
        else:
            return "No"
