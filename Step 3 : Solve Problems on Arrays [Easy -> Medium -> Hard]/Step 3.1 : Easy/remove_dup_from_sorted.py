# https://practice.geeksforgeeks.org/problems/remove-duplicate-elements-from-sorted-array/1

# https://leetcode.com/problems/remove-duplicates-from-sorted-array/submissions/

class Solution:	
	def remove_duplicate(self, A, N):
	    i=0
	    for j in range(1,N):
	        if(A[j]!=A[i]):
	            i+=1
	            A[i]=A[j]
	    return i+1
