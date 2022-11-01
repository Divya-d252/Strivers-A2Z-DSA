# https://practice.geeksforgeeks.org/problems/bubble-sort/1

# https://takeuforward.org/data-structure/bubble-sort-algorithm/

class Solution:
    def bubbleSort(self,arr, n):
        for i in range(n-1):
            for j in range(n-i-1):
                if(arr[j]>arr[j+1]):
                    arr[j],arr[j+1]=arr[j+1],arr[j]
