class Solution:
    def bubbleSort(self,arr, n):
        self.bubble(arr,0)
    def bubble(self,arr,i):
        if(i==n-1):
            return
        for j in range(n-i-1):
            if(arr[j]>arr[j+1]):
                arr[j],arr[j+1]=arr[j+1],arr[j]
        self.bubble(arr,i+1)
