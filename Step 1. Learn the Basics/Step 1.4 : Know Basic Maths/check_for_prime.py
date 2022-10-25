# https://practice.geeksforgeeks.org/problems/composite-and-prime0359/1

# Recursion - prime

def isPrime(n, i):
 
    # Corner cases
    if (n == 0 or n == 1):
        return False
 
    # Checking Prime
    if (n == i):
        return True
 
    # Base cases
    if (n % i == 0):
        return False
 
    i += 1
 
    return isPrime(n, i)
 
 
# Driver Code
if (isPrime(35, 2)):
    print("true")
else:
    print("false")
    
# Brute force -

import math
class Solution:
    def Count(self, L, R):
        p=0
        for i in range(L,R+1):
            c=0
            for j in range(2,int(math.sqrt(i))+1):
                if(i%j==0):
                    c+=1
            if(c==0):
                p+=1
               # print(i)
        if(L==1):
            return R-L+1-(2*p)+1
        else:
            return R-L+1-(2*p)

# https://www.geeksforgeeks.org/sieve-of-eratosthenes/

import math
class Solution:
	def Count(self, L, R):
	    isPrime = [True for i in range(R+1)]
	    for i in range(2,R+1):
	        if(isPrime[i]):
	            for j in range(2*i,R+1,i):
	                isPrime[j]=False
	    p = 0
	    c = 0
	    for i in range(L,R+1):
	        if(i==1):
	            continue
	        if(isPrime[i]):
	            p+=1
	        else:
	            c+=1
	    return c-p
