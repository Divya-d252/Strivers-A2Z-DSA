# https://practice.geeksforgeeks.org/problems/frequency-of-array-elements-1587115620/0

# Time Complexity: O(n). 
# Space Complexity: O(n). 

class Solution:
    def frequencyCount(self, arr, n, P):
        dict1={i:0 for i in arr}
        for i in arr:
            dict1[i]+=1
        arr.clear()
        for i in range(1,N+1):
            if i in dict1:
                arr.append(dict1[i])
            else:
                arr.append(0)
                
# https://www.geeksforgeeks.org/count-frequencies-elements-array-o1-extra-space-time/
                
# Time Complexity: O(n). 
# Space Complexity: O(1). 
                
class Solution:
    def frequencyCount(self, arr, n, P):
        i=0
        while(i<n):
            if(arr[i]<=0):
                i+=1
                continue
            j = arr[i]-1
            if(j>=n):
                arr[i] = 0
                i+=1
            else:
                if(arr[j]>0):
                    arr[i] = arr[j]
                    arr[j] = -1
                else:
                    arr[j] = arr[j] - 1
                    arr[i] = 0
                    i+=1
        for i in range(n):
            arr[i] = abs(arr[i])
