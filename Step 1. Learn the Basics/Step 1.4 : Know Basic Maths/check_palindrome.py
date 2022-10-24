# https://practice.geeksforgeeks.org/problems/palindrome0746/1
  
class Solution:
	def is_palindrome(self, n):
	    if(str(n)==str(n)[::-1]):
	        return "Yes"
	    else:
	        return "No"
