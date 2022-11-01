# https://practice.geeksforgeeks.org/problems/merge-sort/1

#https://takeuforward.org/data-structure/merge-sort-algorithm/

class Solution:
    def merge(self,arr, l, m, r):
        k = l
        i = l
        j = m+1
        l1=[]
        while i <= m and j <= r:
            if arr[i] > arr[j]:
                l1.append(arr[j])
                j+=1
                k+=1
            else:
                l1.append(arr[i])
                i+=1
                k+=1
        while i <= m:
            l1.append(arr[i])
            i+=1
            k+=1
        while j <= r:
            l1.append(arr[j])
            j+=1
            k+=1
        arr[l:r+1]=l1[:]
    def mergeSort(self,arr, l, r):
        if l<r:
            mid = (l+r)//2
            self.mergeSort(arr,l,mid)
            self.mergeSort(arr,mid+1,r)
            self.merge(arr,l,mid,r)
