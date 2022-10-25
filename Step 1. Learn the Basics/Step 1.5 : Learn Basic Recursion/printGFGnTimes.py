# https://practice.geeksforgeeks.org/problems/print-gfg-n-times/1

class Solution:
    def printGfg(self, n):
        if(n==0):
            return
        print("GFG",end=" ")
        Solution.printGfg(self,n-1)
