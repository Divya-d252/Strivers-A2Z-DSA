class Solution:
    def insertionSort(self, arr, n):
        self.insert(arr,1)
    def insert(self,arr,i):
        if(i==n):
            return
        j=i-1
        curr=arr[i]
        while(j>=0 and arr[j]>curr):
            arr[j+1]=arr[j]
            j-=1
        arr[j+1]=curr
        self.insert(arr,i+1)
