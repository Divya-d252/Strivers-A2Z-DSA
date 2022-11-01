# https://practice.geeksforgeeks.org/problems/insertion-sort/0
  
# https://takeuforward.org/data-structure/insertion-sort-algorithm/
  
class Solution:
    def insertionSort(self, arr, n):
        for i in range(1,n):
            j=i-1
            curr=arr[i]
            while(j>=0 and arr[j]>curr):
                arr[j+1]=arr[j]
                j-=1
            arr[j+1]=curr
