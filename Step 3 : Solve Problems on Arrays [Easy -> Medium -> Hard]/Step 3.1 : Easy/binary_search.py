# https://www.geeksforgeeks.org/binary-search/
  
class Solution:
    def binarySearch(self,arr,i,j,K):
        if(i>j):
            return -1
        else:
            mid=(i+j)//2
            if(arr[mid]==K):
                return 1
            elif(arr[mid]>K):
                return self.binarySearch(arr,i,mid-1,K)
            else:
                return self.binarySearch(arr,mid+1,j,K)
    def searchInSorted(self,arr, N, K):
        i=0
        j=N-1
        return self.binarySearch(arr,i,j,K)
