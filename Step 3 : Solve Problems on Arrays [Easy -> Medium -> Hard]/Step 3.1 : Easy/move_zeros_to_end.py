# https://practice.geeksforgeeks.org/problems/move-all-zeroes-to-end-of-array0751/1

# https://takeuforward.org/data-structure/move-all-zeros-to-the-end-of-the-array/

class Solution:
	def pushZerosToEnd(self,arr, n):
	    i=0
	    while(i<n and arr[i]!=0):
    	    i+=1
	    j=i+1
	    while(i<n and j<n):
    	    if(arr[j]!=0):
    	        arr[i],arr[j]=arr[j],arr[i]
    	        i+=1
    	        j+=1
    	    else:
    	        j+=1
