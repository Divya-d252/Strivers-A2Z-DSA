# https://practice.geeksforgeeks.org/problems/largest-element-in-array4009/0

def largest( arr, n):
    maxi=arr[0]
    for i in range(1,n):
        if(arr[i]>maxi):
            maxi=arr[i]
    return maxi
