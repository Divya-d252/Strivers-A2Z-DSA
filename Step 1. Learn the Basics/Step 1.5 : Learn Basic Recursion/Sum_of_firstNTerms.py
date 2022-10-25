# https://practice.geeksforgeeks.org/problems/sum-of-first-n-terms5843/1

# Input:
# N=5
# Output:
# 225
# Explanation:
# 13+23+33+43+53=225

# If we have a series of cubes of n natural numbers as 1**3 + 2**3 + 3**3 + 4**3 + ... + n**3, the formula to find the sum is,
# Sum (S) = {n(n+1)/2}**2

class Solution:
    def sumOfSeries(self,N):
        return ((N*(N+1))//2)*((N*(N+1))//2)
      
# We can use the formula for the sum of N numbers, i.e N(N+1)/2.- 1+2+3...n
