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
        
 class Solution:
    def bubbleSort(self,arr, n):
        self.bubble(arr,0,0)
    def bubble(self,arr,i,j):
        if(i==n-1):
            return
        if(j==n-i-1):
            i+=1
            j=0
        if(arr[j]>arr[j+1]):
            arr[j],arr[j+1]=arr[j+1],arr[j]
        j+=1
        self.bubble(arr,i,j)
