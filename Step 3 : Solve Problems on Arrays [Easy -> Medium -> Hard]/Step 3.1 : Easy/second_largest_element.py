# https://practice.geeksforgeeks.org/problems/second-largest3735/1

class Solution:
	def print2largest(self,arr, n):
	    maxi=float('-inf')
	    second_maxi=float('-inf')
	    for i in range(n):
	        if(arr[i]>maxi):
	            second_maxi=maxi
	            maxi=arr[i]
	        if(arr[i]>second_maxi and arr[i]!=maxi):
	            second_maxi=arr[i]
	    return max(second_maxi,-1)
