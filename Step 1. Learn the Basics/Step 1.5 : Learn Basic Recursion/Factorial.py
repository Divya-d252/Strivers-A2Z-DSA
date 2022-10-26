# https://practice.geeksforgeeks.org/problems/find-all-factorial-numbers-less-than-or-equal-to-n3548/0

class Solution:
    def factorialNumbers(self, N):
        fact = 1
        l=[]
        for i in range(1,N+1):
            fact*=i
            if(fact>N):
                break
            l.append(fact)
        return l
  
# Factorial of a large Number

# Concept - 
# https://www.geeksforgeeks.org/factorial-large-number/
  
# Problem -
# https://practice.geeksforgeeks.org/problems/factorials-of-large-numbers2508/1
  
class Solution:
    def factorial(self, N):
        res = [1]
        arr= [1]
        for i in range(1,N):
            res= Solution.multiply(arr,i+1)
            arr = res[:]
        return res
    
    def multiply(arr,x):
        arr=arr[::-1]
        res=[]
        carry = 0
        for i in range(len(arr)):
            mul = x*arr[i] + carry
            rem = mul%10
            res.append(rem)
            carry = mul//10
        while(carry>0):
            rem = carry%10
            res.append(rem)
            carry = carry//10
        return res[::-1]
