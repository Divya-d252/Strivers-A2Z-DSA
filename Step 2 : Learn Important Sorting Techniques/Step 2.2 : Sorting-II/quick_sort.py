# https://takeuforward.org/data-structure/quick-sort-algorithm/

# https://practice.geeksforgeeks.org/problems/quick-sort/1

# Approach : 
# -> We will be using 2 pointers namely i, j. Initializing i at index 0 and j at index n-1 ( if the length of the array is n ).
# -> We will swap arr[i] and arr[j] if  arr[i] > pivot  and arr[j] < pivot  and will increment i and decrement j . This goes on until i < j . 
# -> Finally when i > j, we will stop swapping arr[i] and arr[j] and swap pivot with arr[j] so that pivot gets its final position.
# -> We will now recursively repeat this process in the left and right of the pivot so that we get our final sorted array.

class Solution:
    def quickSort(self, arr, low, high):
        if (low < high):
            pivot = self.partition(arr, low, high)
            self.quickSort(arr, low, pivot - 1)
            self.quickSort(arr, pivot + 1, high)

    def partition(self, arr, low, high):
        pivot = low
        i = low
        j = high
        while(i<j):
            while (i<high and arr[i] <= arr[pivot]):
                i += 1
            while (j>=low and arr[j] > arr[pivot]):
                j -= 1
            if(i<j):
                arr[i], arr[j] = arr[j], arr[i]
            
        arr[j],arr[low]=arr[low],arr[j]
        return j
